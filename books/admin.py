from django.contrib import admin
from .models import CustomUser, Author, Condition, Genre, Book, WishList

admin.site.register(CustomUser)
admin.site.register(Author)
admin.site.register(Condition)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(WishList)
