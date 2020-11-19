from django.urls import path, re_path
from .views import tube_main, upload_file, watch

urlpatterns = [
    path('', tube_main, name='index'),
    path('upload/', upload_file, name='upload'),
    re_path(r'watch/(?P<vid>\w*)', watch)
]
