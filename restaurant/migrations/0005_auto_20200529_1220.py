# Generated by Django 3.0.6 on 2020-05-29 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_restaurant_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='description',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='description',
            field=models.CharField(max_length=5000),
        ),
    ]
