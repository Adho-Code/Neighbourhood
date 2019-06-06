from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

# Create your views here.
def homm(request,id):

    biz = Business.objects.all()

    post = Post.objects.filter(hood_id=id)

    activ = Activities.objects.all()

    post = Post.objects.filter(hood_id=id)
    return render(request, 'home.html', locals())

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = UserCreationForm()

    return render(request,'signup.html',locals())

def search_business(request):
    
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_business = Business.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',locals())

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',locals())


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
    post = Post.objects.all()
    hood = NeighbourHood.objects.all()
    return render(request,'location.html')

@login_required
def post(request):
    if request.method == 'POST':
        form = MakePostForm(request.POST,request.FILES)

        if form.is_valid():
            post=form.save(commit=False)
            post.save()
        return redirect('home',1)
    else:
        form  = MakePostForm()
    return render(request,'post.html',locals())

# @login_required
# def search_business(request):

#     if 'business' in request.GET and request.GET["business"]:
#         search_term = request.GET.get("business")
#         searched_business = Business.search_by_business_name(search_term)
#         message = f"{search_term}"

#         return render(request, 'search.html',locals())

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'search.html',locals())

def profile(request):
    profile=Profile.objects.filter(user_id=request.user)
    
    return render(request, 'profile.html',{'profile':profile})


def update(request):
    all_profile = Profile.objects.all()
    profile = Profile.objects.get(user_id = request.user)
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form  = ProfileForm()

    return render(request,'new_profile.html', locals())


def editprofile(request):
    
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
    
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user_id=request.user
            profile.save()
            return redirect('profile',request.user.id)
    else:
        form =ProfileForm()
        
    return render(request,'editprofile.html',locals())


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

def biz(request):
    if request.method == 'POST':
        form = BizForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
        return redirect('home',1)
    else:
        form  = BizForm()
    return render(request,'business.html',locals())


def activ(request):
    if request.method == 'POST':
        form = ActivForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
        return redirect('home',1)
    else:
        form  = ActivForm()
    return render(request,'activities.html',locals())