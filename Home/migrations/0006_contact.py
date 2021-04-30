# Generated by Django 3.1.7 on 2021-04-19 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_auto_20210327_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msgid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('email', models.TextField(max_length=300)),
                ('phone', models.TextField(default='', max_length=300)),
                ('desc', models.TextField(max_length=300)),
            ],
        ),
    ]