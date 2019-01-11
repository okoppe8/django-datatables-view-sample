from django.urls import path
from django.views.generic.base import TemplateView

from . import views

app_name = 'sample'

urlpatterns = [
    path('', TemplateView.as_view(template_name='sample/index.html'), name='index'),
    path('sample01', TemplateView.as_view(template_name='sample/sample01.html'), name='sample01'),
    path('sample02', TemplateView.as_view(template_name='sample/sample02.html'), name='sample02'),
    path('items', views.ItemsJsonView.as_view(), name='ItemsJson'),
    path('print', views.PrintView.as_view(), name='print'),
    path('excel', views.ExcelView.as_view(), name='excel'),
    path('csv', views.CsvView.as_view(), name='csv'),
]
