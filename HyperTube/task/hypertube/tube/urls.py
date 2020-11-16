from django.urls import path
from .views import tube_main

urlpatterns = [
    path('', tube_main)
]
