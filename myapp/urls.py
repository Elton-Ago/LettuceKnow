from django.urls import path
from . import views

urlpatterns = [
    #'' is root url, and render index file
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('post/<str:pk>', views.post, name='post')
    #if /download was in the quotes for path it would take the user to the downloads url
]