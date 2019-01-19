from django.urls import path, re_path
from . import views

app_name = 'object'

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('upload/push_upload/', views.SaveImage, name = 'save_image')

  ]
