from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='task-list'),  # List all tasks or create a new one
    path('<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),  # Retrieve, update, or delete a specific task
]