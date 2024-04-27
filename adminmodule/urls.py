from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
     path('',views.projecthomepage,name = 'projecthomepage'),
     path('servicehomepage',views.servicehomepage,name = 'servicehomepage'),
     path('userhomepage',views.userhomepage,name = 'userhomepage'),
     path('signup',views.signup,name='signup'),
     path('signup1', views.signup1, name='signup1'),
     path('login',views.login,name='login'),
     path('login1',views.login1,name='login1'),
     path('logout',views.logout,name='logout')

]
