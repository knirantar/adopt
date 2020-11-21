from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('home/adoption/',views.adoption,name = 'adoption'),
    path('home/volunteer/',views.volunteer,name = 'volunteer'),
    path('home/stories/',views.stories,name = 'stories'),
    path('home/donation/',views.donation,name = 'donation'),
    path('home/about/',views.about,name = 'about'),
    path('home/contact/',views.contact,name = 'contact'),
    path('home/checklist/',views.checklist,name = 'checklist'),
    path('home/help/',views.help,name = 'help'),
    path('home/faq/',views.faq,name = 'faq'),
    path('home/adoption/adoption_dog/',views.adoption_dog,name = 'adoption_dog'),
    path('home/adoption/adoption_dog/details/<str:pk>/',views.details,name = 'details'),
    path('home/adoption/adoption_cat/',views.adoption_cat,name = 'adoption_cat'),
    path('home/adoption/adoption_others/',views.adoption_others,name = 'adoption_others'),
    path('home/stories/storydetails/<str:pk>/',views.storydetails,name = 'storydetails'),
    
]
