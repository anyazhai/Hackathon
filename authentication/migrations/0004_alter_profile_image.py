# Generated by Django 4.0.3 on 2022-03-08 22:27

import authentication.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_profile_image_profile_join_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profiles/default_zayg9d.jpg', upload_to=authentication.models.user_directory_path),
        ),
    ]