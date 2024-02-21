from .models import Book, WishList, Author, Genre, Condition, CustomUser
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title']


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class WishListSerializer(serializers.ModelSerializer):
    pickup_location = serializers.SerializerMethodField()
    class Meta:
        model = WishList
        fields = ['id', 'user', 'book', 'status', 'pickup_location']
        read_only_fields = ['user']

    def create(self, validated_data):
        # iuseris fields gautolebs requestis gamomgzavn users 
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user.username
        representation['book'] = instance.book.title
        return representation
    
    def get_pickup_location(self, obj):
        user = self.context['request'].user
        if (obj.book.owner == user or user.is_staff):
            return obj.book.pickup_location
        else:
            return "Access Forbidden"
    
    
    def update(self, instance, validated_data):
        # axdens ganaxlebas
        instance = super().update(instance, validated_data)

        # if amowmebs Tu statusi gaxdeba sumbitted
        if instance.status == "submitted":
            # anaxlebs wignis mflobels submitted statusis Semdeg mflobeli gaxdeba is visac surda
            if instance.book_id:
                first_book = instance.book
                first_book.owner = instance.user
                first_book.save()

        return instance