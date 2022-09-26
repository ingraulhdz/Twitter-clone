from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.

def index(request):
    #if the method is post
   

    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')

        #if the form is valid 
        else:
           return HttpResponseRedirect(form.errors.as_json())
        #save


        # no redirect error
    #get posts
    
    posts = Post.objects.all()[:20]
  
    return render(request, 'posts.html', {'posts':posts})

def delete(reqeust, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')


def likes(request, post_id):
    post = Post.objects.get(id=post_id)
    post.like+=1
    post.save()
    return HttpResponseRedirect('/')


def edit(request, post_id):
    #if the method is post
    post = Post.objects.get(id=post_id)
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')

        #if the form is valid 
        else:
           return HttpResponseRedirect(form.errors.as_json())
        #save


        # no redirect error
    #get posts
    

  
    return render(request, 'edit.html', {'post':post})