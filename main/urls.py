from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('classes/', views.classes, name='classes'),
    path('display_class/<class_id>', views.display_class, name='display_class'),
    path('add_class/', views.add_class, name='add_class'),
    path('update_class/<class_id>', views.update_class, name='update_class'),
    path('delete_class/<class_id>', views.delete_class, name='delete_class'),
    path('tasks/', views.tasks, name='tasks'),
    path('add_task/', views.add_task, name='add_task'),
    path('update_task/<task_id>', views.update_task, name='update_task'),
    path('delete_task/<task_id>', views.delete_task, name='delete_task'),
    path('display_task/<task_id>', views.display_task, name='display_task'),
    path('search/',views.search, name='search'),
]