from django.shortcuts import render
from .models import Video
# Create your views here.


def tube_main(request):
    videos = Video.objects.all()
    return render(request, 'tube_main.html', {'videos': videos})
