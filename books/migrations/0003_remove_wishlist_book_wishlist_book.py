# Generated by Django 5.0.1 on 2024-02-20 22:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_remove_wishlist_user_wishlist_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='book',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='books.book'),
            preserve_default=False,
        ),
    ]
