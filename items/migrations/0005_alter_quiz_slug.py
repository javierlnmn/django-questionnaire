# Generated by Django 4.2 on 2024-08-28 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_quiz_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
