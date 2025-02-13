

from django.urls import path
from .views import add_task, get_tasks, task_detail  

urlpatterns = [
    path('tasks/', get_tasks, name='get_tasks'),  
    path('tasks/add/', add_task, name='add_task'), 
    path('tasks/<int:task_id>/', task_detail, name='task_detail'), 
]

