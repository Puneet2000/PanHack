from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'object'

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('upload/push_upload/', views.SaveImage, name = 'save_image'),
    path('government/', views.welcome),
    re_path('status/(?P<issue_id>\d+)/$', views.get_status),
    path('login/', views.login, name ='login'),
    path('worker_login/', views.worker_login, name = 'worker_login'),
    path('comments/', views.comments, name = 'comments'),
    path('comments/save_comments/', views.save_comments, name='save_comments'),
    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
