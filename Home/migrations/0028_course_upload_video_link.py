# Generated by Django 3.1.7 on 2021-04-30 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0027_auto_20210426_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_upload',
            name='video_link',
            field=models.CharField(default='', max_length=800),
        ),
    ]
