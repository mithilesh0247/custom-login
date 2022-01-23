from . import views
from django.urls import path,include
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('', views.home),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('logout/', views.logout_view,  name="logout"),
    # path('', include('social_django.urls', namespace='social')),
    path('', include('social_django.urls', namespace='social')),
]
