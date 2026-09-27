from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
# Create your views here.
def index(request):
    myposts = Blog.objects.all()
    print(myposts)
    return render(request, "blog/index.html",{'myposts':myposts})

def blogpost(request, id):
    post = Blog.objects.filter(post_id=id)[0]

    try:
        prevpost = Blog.objects.filter(post_id__lt=id).order_by('-post_id')[0]
    except:
        prevpost = None

    try:
        nextpost = Blog.objects.filter(post_id__gt=id).order_by('post_id')[0]
    except:
        nextpost = None

    return render(request, "blog/blogpost.html", {
        'post': post,
        'prevpost': prevpost,
        'nextpost': nextpost
    })