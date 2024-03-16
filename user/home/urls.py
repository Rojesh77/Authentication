from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('',views.signup,name='signup'),
    path('home/',views.index,name='home'),
    path('signup',views.signup,name='signup'),
    path("login",views.loginuser,name='login'),
    path("logout/",views.logoutuser,name='logout')
   
]
