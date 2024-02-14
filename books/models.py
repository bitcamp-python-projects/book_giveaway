from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):  # აქ როლები განვსაზღვრე
    ROLE_CHOICES = (
        ('administrator', 'Administrator'),
        ('owner', 'Owner'),
        ('user', 'User'),
    )

    role = models.CharField(max_length=15, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username


class Author(models.Model):  # ავტორების მოდელი
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.author


class Condition(models.Model):  # წიგნის მდგომარეობის მოდელი (მაგ. ახალი, ძველი)
    condition = models.CharField(max_length=100)

    def __str__(self):
        return self.condition


class Genre(models.Model):  # ჟანრები
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Book(models.Model):  # წიგნების მოდელი
    title = models.CharField(max_length=50)
    author = models.ManyToManyField(Author)
    genre = models.ManyToManyField(Genre)
    condition = models.ManyToManyField(Condition)
    image = models.ImageField(upload_to='images/')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    pickup_location = models.TextField()

    def __str__(self):
        return self.title


class WishList(models.Model):  # სასურველი წიგნების მოდელი
    STATUS_CHOICES = (  # განსაზღვრულია როლ სტატუსები 
        ('pending', 'pending'), # სანამ owner დაასაბმითებს ვის მისცეს წიგნი როცა რამდენიმე მოთხოვნაა
        ('submitted', 'submitted'),  # მას შემდეგ რაც owner აირჩევს ადრესატს
    )
    user = models.ManyToManyField(CustomUser) 
    book = models.ManyToManyField(Book)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.user} - {self.book}"
