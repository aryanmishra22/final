# Generated by Django 4.1.4 on 2023-04-01 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final_web', '0004_alter_post_body_postvideos_posturls_postimages_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=1000),
        ),
    ]
