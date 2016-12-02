from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
# Create your views here.

def welcome(request):
    return render(request,'welcome.html')

def index(request):
    post_lists = Article.objects.all() 
    return render(request, 'index.html', {'post_lists':post_lists})

def detail(request, num):
    try:
        post_list = Article.objects.get(id = int(num))
        return render(request, 'detial.html', {'post_list': post_list})
    except Exception as e:
        print(e)
    return HttpResponse(num)