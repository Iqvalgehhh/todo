#a18
from django.urls import path
from . import views

#a19
urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
]