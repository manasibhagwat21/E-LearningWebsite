# Generated by Django 3.1.7 on 2021-04-21 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0016_auto_20210421_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_files',
            name='notes_file',
            field=models.FileField(upload_to='Material/Javascript'),
        ),
        migrations.AlterField(
            model_name='upload_files',
            name='video_file',
            field=models.FileField(upload_to='Material/Javascript'),
        ),
    ]
