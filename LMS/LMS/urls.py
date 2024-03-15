"""
URL configuration for LMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .import views , user_login
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin', admin.site.urls),
    path ('', views.HOME, name='home' ),
    path('404', views.PAGE_NOT_FOUND , name='404'),
    path('course/', views.COURSE, name='course'),
    path('single/course', views.SINGLE_COURSE, name='single_course'),
    path('course/<slug:slug>', views.COURSE_DETAILS, name='course_details'),
    path('search', views.SEARCH_COURSE, name='search_course'),
    path('contact', views.CONTACT_US, name='contact_us'),
    path('about', views.ABOUT_US, name='about_us'),
    path('team', views.TEAM, name='team'),
    path('accounts/register',user_login.REGISTER, name='register' ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('doLogin', user_login.DO_LOGIN, name='doLogin'),
    path('accounts/profile',user_login.PROFILE, name='profile' ),
    path('accounts/profile/update',user_login.PROFILE_UPDATE, name='profile_update' ),
    path('checkout/<slug:slug>', views.CHECKOUT, name='checkout'),
    path('my_course', views.MY_COURSE, name='my_course'),
    path('course/watch_course/<slug:slug>',  views.WATCH_COURSE, name='watch_course'),
    path('sidebar', views.SIDEBAR, name='sidebar'),
    path('main_profile', views.MAIN_PROFILLE, name='main_profile'),
    path('notice', views.NOTICE, name='notice'),
    path ('all_course', views.ALL_COURSE, name='all_course'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
