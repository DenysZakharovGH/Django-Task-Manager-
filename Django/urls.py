"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from task import views
from django.contrib.auth import views as auth_views

from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('task/<int:id>', views.show_Class_Task),

    path('task/<int:id>/edit/', views.edit_Class_Task),

    path('task/<int:id>/confirm/', views.confirm_Class_Task),

    path('task/<int:id>/delete/', views.delete_task),

    path('task/<int:id>/<int:id_chek_list>/', views.show_ChekList),

    path('task/<int:id>/<int:id_chek_list>/delete_CheckItem/', views.delete_CheckItem),

    path('task/<int:id>//NewChek', views.add_ChekList),

    path('login/', auth_views.LoginView.as_view()),

    path('accounts/login/', auth_views.LoginView.as_view()),

    path('logout/', auth_views.LogoutView.as_view()),

    path('register/', views.register),

    path('reset_user/', views.reset_user),

   # path('sendEmail/', views.send_mail()),

    path('password_reset_email/', views.MyPasswordResetView, name='password_reset'),

    path('password_reset/', views.MyPasswordResetView, name='password_reset'),

    path('', views.index),

    path('home/', views.index),

    path('task/new/', views.add_new_task),
]