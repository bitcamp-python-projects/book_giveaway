from django.contrib import admin
from django.contrib.auth.hashers import make_password
from .models import CustomUser, Author, Condition, Genre, Book, WishList

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Ensure password is hashed before saving
        if obj.password:
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)



admin.site.register(Author)
admin.site.register(Condition)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(WishList)

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Ensure password is hashed before saving
        if obj.password:
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)

admin.site.register(User, UserAdmin)

