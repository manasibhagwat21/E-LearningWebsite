# Generated by Django 3.1.7 on 2021-04-21 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0011_auto_20210420_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file_field',
            field=models.FileField(upload_to='static/'),
        ),
    ]
