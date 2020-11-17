from django.shortcuts import render
from .models import Video, VideoTag, Tag
# Create your views here.


def tube_main(request):
    context = {}
    if request.GET.get('tag') is not None:
        tag = request.GET.get('tag')
        videos = Video.objects.filter(videotag__tag__name=tag)
        context['tag'] = '#' + tag
    elif request.GET.get('q') is not None:
        q = request.GET.get('q')
        videos = Video.objects.filter(title=q)

    else:
        videos = Video.objects.all()
    # print(videos.values())
    context['videos'] = videos  # = Video.objects.all()
    return render(request, 'tube_main.html', context)
