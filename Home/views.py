from django.contrib import auth, messages
from django.db import models
from django.views.generic.list import ListView
from .models import Contact, faculty, Upload_Files , course_upload
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
import os


# Maria@20
# Create your views here.s


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def index(request):
    return render(request, 'index.html')


def loginU(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        phone = request.POST.get('phone')
        if password == cpassword:
            user = User(username=username, password=password)
            user.save()
            return render(request, 'login1.html')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


def logoutU(request):
    auth.logout(request)
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def catalog(request):
    return render(request, 'catalog.html')


def catalog_faculty(request):
    return render(request, 'catalog_faculty.html')


def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contactus = Contact(name=name, email=email, phone=phone, desc=desc)
        contactus.save()
        # print(name)
    return render(request, 'Contactus.html')


def c1(request):
    return render(request, 'c1.html')


def c2(request):
    return render(request, 'c2.html')


def c3(request):
    return render(request, 'c3.html')


def c4(request):
    return render(request, 'c4.html')


def c5(request):
    return render(request, 'c5.html')


def c6(request):
    return render(request, 'c6.html')


def resources(request):
    # path="C:\\Users\\Kevin\\PycharmProjects\\E-LearningWebsite\\static\\Material"
    all_Materials = Upload_Files.objects.all()
    return render(request, 'resources.html', {"Materials": all_Materials})

def course(request):
    # path="C:\\Users\\Kevin\\PycharmProjects\\E-LearningWebsite\\static\\Material"
    m = course_upload.objects.all()
    return render(request, 'course.html', {"courses": m})


def login_faculty(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if faculty.objects.filter(username=username, password=password):
            teacher = faculty.objects.get(username=username)
            faculty.save()
            return redirect('catalog_faculty.html')

        else:
            messages.info(request, "Invalid Credentials")
            return redirect('/login_faculty.html')

    return render(request, 'login_faculty.html')


def login1(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'catalog.html')
        else:
            return render(request, 'login1.html')

    return render(request, 'login1.html')


# class UploadView(ListView):
#     def get(self, request, user_name):
#         return render(request, 'main/upload_file.html')
#
#
#     def post(self, request, user_name):
#         filename = request.FILES['filename']
#         title = request.POST['title']
#         desc = request.POST['desc']
#
#         user_obj = faculty.objects.get(username=user_name)
#         upload_post = Post(user=user_obj, title=title, file_field=filename, desc=desc)
#         upload_post.save()
#         messages.success(request, 'Your Post has been uploaded successfully.')
#         return render(request, 'main/upload_file.html')

def upload_file(request):
    files = Upload_Files.objects.all()
    if request.method == "POST":
        topic_name = request.POST.get('topic_name')
        # video_file = request.FILES.get('video_file')
        notes_file = request.FILES.get('notes_file')

        file = Upload_Files.objects.create(topic_name=topic_name, notes_file=notes_file)

        file.save()
        return redirect('catalog_faculty')

    return render(request, 'upload_file.html', {"files": files})


def upload_c(request):
    files = course_upload.objects.all()
    if request.method == "POST":
        topic_name = request.POST.get('topic_name')
        desc = request.POST.get('desc')
        video_link = request.POST.get('video_link') 
        notes_file = request.FILES.get('notes_file')

        file = course_upload.objects.create(topic_name=topic_name, desc=desc,video_link=video_link, notes_file=notes_file)

        file.save()
        return redirect('resources.html')

    return render(request, 'upload_c.html', {"files": files})