# Generated by Django 4.2.4 on 2023-08-19 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='recommended',
            field=models.BooleanField(default=True),
        ),
    ]
