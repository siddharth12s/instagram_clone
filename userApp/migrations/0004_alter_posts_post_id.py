# Generated by Django 4.2.2 on 2023-06-21 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0003_remove_posts_is_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]