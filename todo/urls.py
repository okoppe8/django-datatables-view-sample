from django.urls import path, include
from rest_framework import routers

from . import views
from .views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)

app_name = 'todo'

urlpatterns = [
    path('', views.MainView.as_view(), name='index'),
    path('api/datatables', views.TasksJsonView.as_view(), name='TasksJson'),
    path('api/', include(router.urls)),
]
