"""
URL configuration for myweb1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from myweb1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('info/', views.info),
    path('', views.default_page),
    path("test/", views.test),
    # path('info/<int:sid>', views.posts),
    path('info/<sid>', views.posts),
    path('myhome/', views.myhome),
    path('index/', views.index),
    path('djangohome/', views.djangohome),
    path('homepass/', views.homepass),
    path('mygetform/', views.mygetform),
    path('mypostform/', views.mypostform),
    path('actionsubmit', views.actionsubmit,name = "actionsubmit"),
    path('renderpage/', views.renderpage),
    path('redirectform/', views.redirectform),
]
