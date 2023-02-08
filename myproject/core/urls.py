from django.urls import path
from .views import *
urlpatterns = [
    path('', index , name='index'),
    path('all/' , TodoListView.as_view() , name='all_todos'),
    path('add/' , TodoCreateView.as_view() , name='add_todos'),
    path('todo/<int:pk>/',TodoDetailView.as_view(), name='todo_detial'),
    path('edit/<int:pk>/',TodoUpdateView.as_view(), name='update_detial'), 
    path('delete/<int:pk>/',TodoDeleteView.as_view(), name='delete_todo'),

]
