from django.urls import path
from .views import tube_main, upload_file

urlpatterns = [
    path('', tube_main),
    path('upload/', upload_file),
]
