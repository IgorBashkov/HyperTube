from django.shortcuts import render
from .models import Video
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
# Create your views here.


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'http://127.0.0.1:8000/login/'
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
