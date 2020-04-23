from django.urls import path

from .views import TasksView
app_name="tasks"

urlpatterns = [
    path('', TasksView.as_view(), name='crud'),
    path('<int:pk>', TasksView.as_view(), name='crud_pk'),
]