# Generated by Django 2.0.1 on 2018-01-28 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0005_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, upload_to='car_images'),
        ),
        migrations.AlterField(
            model_name='car',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]