from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Profile,Art,Comments,Category
from django.contrib.auth.decorators import login_required
from .forms import NewArtForm,NewProfileForm,CommentForm

# Create your views here.

def index(request):
    ones_art = Art.objects.all()
    all_arts = Art.get_all_arts()
    categories = Category.get_categories()
    print(categories)
    return render(request, 'index.html', {"all_arts": all_arts, "ones_art":ones_art, "categories": categories})

def image_category(request, category):
    images = Art.filter_by_category(category)
    print(images)
    return render(request, 'category.html', {'category_images': images})

@login_required(login_url='/accounts/login/')
def upload_art(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewArtForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('index')
    else:
        form = NewArtForm()
    return render(request, 'upload_art.html', {"form": form})


def one_art(request,id):
    ones_art = Art.objects.filter(id = id)
    return render(request,'art.html',{"ones_art":ones_art,}) 

@login_required(login_url='accounts/login/')
def add_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(id = current_user.id)
    if request.method == 'POST':
        form = NewArtForm(request.POST, request.FILES)
        if form.is_valid():
            caption = form.save(commit=False)
            caption.user = current_user
            caption.save()
            return redirect('myprofile')
    else:
        form = NewArtForm()
    return render(request, 'edit_profile.html', {"form":form})  

@login_required(login_url='accounts/login/')
def my_profile(request):
    current_user = request.user
    my_arts = Art.objects.filter(user = current_user)
    my_profile = Profile.objects.filter(user = current_user).first
    return render(request, 'profiles.html', {"my_arts": my_arts, "my_profile":my_profile})

def search_art(request):
    if 'art_name' in request.GET and request.GET["art_name"]:
        search_term = request.GET.get("art_name")
        searched_art = Art.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, "search.html",{"message":message,"art": searched_project})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def add_comment(request, art_id):
    current_user = request.user
    art_item = Art.objects.filter(id = art_id).first()
    profiless = Profile.objects.filter(user = current_user.id).first()
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.posted_by = profiless
            comment.commented_art = art_item
            comment.save()
            return redirect('oneart',art_id)
    else:
        form = CommentForm()
    return render(request, 'comment_form.html', {"form": form, "art_id": art_id})


def comment(request, id):
    mycomments = Comments.objects.filter(commented_art = id).all()
    return render(request, 'comments.html', {"mycomments":mycomments})








