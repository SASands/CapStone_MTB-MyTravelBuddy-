# Generated by Django 4.0.4 on 2022-05-20 19:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Friends', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='friends',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
