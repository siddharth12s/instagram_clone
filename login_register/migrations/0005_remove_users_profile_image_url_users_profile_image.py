# Generated by Django 4.2.2 on 2023-06-25 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_register', '0004_alter_users_managers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='profile_image_url',
        ),
        migrations.AddField(
            model_name='users',
            name='profile_image',
            field=models.ImageField(blank=True, default='static/images/default_profile_pic/Default_pfp.jpg', upload_to='profile_images/'),
        ),
    ]
