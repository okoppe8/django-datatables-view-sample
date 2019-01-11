# Create your views here.
from django.views.generic import FormView
from django_datatables_view.base_datatable_view import BaseDatatableView
from rest_framework import serializers
from rest_framework import viewsets

from .models import Task
from .forms import TaskForm

class MainView(FormView):
    template_name = 'todo/index.html'
    form_class = TaskForm


class TasksJsonView(BaseDatatableView):
    # モデルの指定
    model = Task
    # フィールドの指定
    columns = ['id', 'status', 'title', 'detail', 'created_at', 'updated_at']

    # 検索方法の指定：部分一致
    def get_filter_method(self):
        return super().FILTER_ICONTAINS

    def get_initial_queryset(self):
        return Task.objects.filter(is_deleted=False)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
