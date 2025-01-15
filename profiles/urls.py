from django.urls import path
from tasks import views

urlpatterns = [
    path('tasks/', views.TaskList.as_view(), name='task-list'),  # List all tasks or create a new task
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),  # Retrieve, update, or delete a specific task
]