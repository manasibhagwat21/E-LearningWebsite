# Generated by Django 3.1.7 on 2021-04-21 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0014_delete_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload_files',
            name='lecture_no',
        ),
        migrations.AlterField(
            model_name='upload_files',
            name='notes_file',
            field=models.FileField(upload_to='Material/'),
        ),
        migrations.AlterField(
            model_name='upload_files',
            name='video_file',
            field=models.FileField(upload_to='Material/'),
        ),
    ]
