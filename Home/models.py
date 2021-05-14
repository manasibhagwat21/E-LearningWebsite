from django.db import models
from django.db.models import When


# Create your models here.
# class Student(models.Model):
#     username = models.CharField(max_length=300, unique=True)
#     password = models.TextField(default='abc123')
#     cpassword = models.TextField(default='abc123')
#     email = models.TextField()
#     firstname = models.TextField(default='asc')
#     lastname = models.TextField(default='asc')

class Contact(models.Model):
    msgid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, default='')
    email = models.CharField(max_length=300, default='')
    phone = models.CharField(max_length=300, default='')
    desc = models.CharField(max_length=300, default='')


class faculty(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Upload_Files(models.Model):
    topic_name = models.CharField(max_length=200)
    notes_file = models.FileField(upload_to="Material/")


class course_upload(models.Model):
    topic_name = models.CharField(max_length=200)
    slug=models.SlugField()
    desc = models.CharField(max_length=500)
    notes_file = models.FileField(upload_to="Material/")
    video_link = models.CharField(max_length=800,default='')

