from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

# Create your views here.
def homm(request,id):

    activ = Activ.objects.filter(neighborhood_id=id)

    post = Post.objects.filter(hoodies_id=id)

    return render(request,'home.html', locals())

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = UserCreationForm()

    return render(request,'signup.html',locals())

def hood(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
        return redirect('location')
    else:
        form  = NeighbourHoodForm()
    return render(request,'hood.html',locals())

def location(request):
    hood = NeighbourHood.objects.all()
    return render(request,'location.html',locals())

@login_required
def post(request):
    if request.method == 'POST':
        form = MakePostForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
        return redirect('home',request.user.profile.neighborhood_id.id)
    else:
        form  = MakePostForm()
    return render(request,'post.html',locals())

@login_required
def search_business(request):

    if 'activity' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_activity = Activity.search_by_activity_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',locals())

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',locals())


def profile_index(request):
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form =UploadForm()


        all_profile = UserProfile.objects.all()
    return render(request,'profile.html', locals())


def update_index(request):
    # all_profile = Profile.objects.all()
    profile = UserProfile.objects.get(user_id = request.user)
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form  = UploadForm()

    return render(request,'new.html', locals())

def activ(request):
    if request.method == 'POST':
        form = ActivForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
        return redirect('location')
    else:
        form  = ActivForm()
    return render(request,'activity.html',locals())
