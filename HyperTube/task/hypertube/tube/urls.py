from django.urls import path, re_path
from .views import tube_main, upload_file, watch, video_loader

urlpatterns = [
    path('', tube_main, name='index'),
    path('upload/', upload_file, name='upload'),
    re_path(r'watch/(?P<id>\w+)', watch),
    re_path(r'(?P<vid>\w+\.\w+/$)', video_loader),
]
