# Generated by Django 4.1.4 on 2023-03-05 07:15

from django.db import migrations, models
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('final_web', '0002_comments_organization_position_post_profile_votes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=martor.models.MartorField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
    ]
