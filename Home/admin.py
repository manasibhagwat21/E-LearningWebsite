from django.contrib import admin

# Register your models here.
from .models import Contact, faculty, Upload_Files, course_upload

admin.site.register(Contact)


@admin.register(faculty)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password']


# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['user', 'title', 'file_field']

admin.site.register(Upload_Files)
admin.site.register(course_upload)
