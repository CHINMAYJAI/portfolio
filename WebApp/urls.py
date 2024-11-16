from django.contrib import admin
from django.urls import path,include
from WebApp import views

urlpatterns = [
    path('home/', views.home ,name="home"),
    path('about/',views.about,name="about"),
    path('experience/',views.experience,name="experience"),
    path('project1/',views.project1,name="project1"),
    path('project2/',views.project2,name="project2"),
    path('contact/', views.contact ,name="contact"),
    path('thanking_page/', views.thankingPage ,name="thanking_page")
]