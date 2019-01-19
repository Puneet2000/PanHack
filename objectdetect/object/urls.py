from django.urls import path, re_path
from . import views

app_name = 'object'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('responses/', views.responses, name='responses'),
]
