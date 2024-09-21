#a18
from django.urls import path
from . import views

#a19
urlpatterns = [
    #add task
    path('addTask/', views.addTask, name='addTask'),
    #a28
    #mark as done
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    #a31
    #mark as undone
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),
    #a33
    #edit feature
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    #a40
    #delete feature
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
    



]