from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):  # Define roles for users
    ROLE_CHOICES = (
        ('administrator', 'Administrator'),
        ('owner', 'Owner'),
        ('user', 'User'),
    )

    role = models.CharField(max_length=15, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username


class Author(models.Model):  # Books' auhors' model
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.author


class Condition(models.Model):  # Book's condition (new, old, ect.)
    condition = models.CharField(max_length=100)

    def __str__(self):
        return self.condition


class Genre(models.Model):  # Books' genres
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Book(models.Model):  # Books model
    title = models.CharField(max_length=50)
    author = models.ManyToManyField(Author)
    genre = models.ManyToManyField(Genre)
    condition = models.ManyToManyField(Condition)
    image = models.ImageField(upload_to='images/')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    pickup_location = models.TextField()

    def __str__(self):
        return self.title


class WishList(models.Model):  # Wishlist model
    STATUS_CHOICES = (  # Defines status choices:
        ('pending', 'pending'), # pending - before owner sumbites where there're more requests then one
        ('submitted', 'submitted'),  # submitted - after the owner chose
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.user} - {self.book}"
    
    