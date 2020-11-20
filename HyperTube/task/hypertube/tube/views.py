from django.shortcuts import render, redirect
from .models import Video, Tag, VideoTag
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import UploadVideoForm
from hypertube.settings import MEDIA_ROOT
from django.http import HttpResponse
# Create your views here.


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'http://localhost:8000/login/'
    template_name = 'signup.html'


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
    context['videos'] = videos
    return render(request, 'tube_main.html', context)


def upload_file(request):
    if request.method == 'POST':
        form = UploadVideoForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            f = data['video']
            vid = Video.objects.create(
                title=data['title'],
                file=f.name,
            )
            for tag in data['tags'].split():
                tg = Tag.objects.create(name=tag)
                VideoTag.objects.create(tag=tg, video=vid).save()
            vid.save()
            tg.save()
            with open(MEDIA_ROOT + f.name, 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
            return redirect('index')

    else:
        form = UploadVideoForm
    return render(request, 'upload.html', {'form': form})


def watch(request, **kwargs):
    context = {}
    video = Video.objects.get(id=kwargs['id'])
    context['video'] = video
    context['type'] = video.file.split('.')[-1]
    context['tags'] = Tag.objects.filter(videotag__video=video)
    return render(request, 'watch.html', context)


def video_loader(request, **kwargs):
    video = open(MEDIA_ROOT.replace('/', '\\') + kwargs['vid'][:-1], 'rb')
    response = HttpResponse(video, content_type='video/' + kwargs['vid'][:-1].split('.')[-1])
    response['Accept-Ranges'] = 'bytes'
    return response
