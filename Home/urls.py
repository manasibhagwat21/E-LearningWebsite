from django.contrib import admin
from django.urls import path
from Home import views
from django.conf.urls import url

urlpatterns = [
  #  path('admin/', admin.site.urls),
    #path('login', views.loginU,name = 'login'),
    path('logout', views.logoutU,name = 'logout'),
    path('login1.html', views.login1,name = 'login1'),
    path('', views.index,name = 'index'),
    path('aboutus', views.aboutus,name = 'aboutus'),
    path('catalog', views.catalog,name = 'catalog'),
    path('contactus', views.contactus,name = 'contactus'),
    path('c1.html', views.c1,name = 'c1.html'),
    path('c2.html', views.c2,name = 'c2.html'),
    path('c3.html', views.c3,name = 'c3.html'),
    path('c4.html', views.c4,name = 'c4.html'),
    path('c5.html', views.c5,name = 'c5.html'),
    path('c6.html', views.c6,name = 'c6.html'),
    path('resources.html', views.resources, name='resources.html'),
    path('signup.html', views.signup,name = 'signup.html'),
    path('upload_file.html', views.upload_file, name='upload_file'),
    path('upload_c.html', views.upload_c, name='upload_c'),
    path('course.html', views.course, name='course.html'),
    path('login_faculty.html', views.login_faculty,name = 'login_faculty.html'),
    path('faculty_options.html', views.faculty_options,name = 'faculty_options.html'),
    path('catalog_faculty.html', views.catalog_faculty,name = 'catalog_faculty'),
    url(r'^(?P<link>[\w-]+)/$', views.coursePage, name='coursePage'),
]

