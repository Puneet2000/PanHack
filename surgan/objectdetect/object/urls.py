from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'object'

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('upload/push_upload/', views.SaveImage, name = 'save_image'),
    path('government/', views.welcome, name = 'government'),
    path('login/', views.login, name ='login'),
    path('worker_login/', views.worker_login, name = 'worker_login'),

  ]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
