from django.shortcuts import render
from .models import Video, Tag, VideoTag
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import UploadVideoForm
from hypertube.settings import MEDIA_ROOT
from django.shortcuts import redirect
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
    # print(videos.values())
    context['videos'] = videos  # = Video.objects.all()
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
            tg = Tag.objects.create(name=data['tags'])
            VideoTag.objects.create(tag=tg, video=vid).save()
            vid.save()
            tg.save()
            with open(MEDIA_ROOT + f.name, 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
            # response = HttpResponseRedirect('/tube/')
            return redirect('index')

    else:
        form = UploadVideoForm
    return render(request, 'upload.html', {'form': form})




