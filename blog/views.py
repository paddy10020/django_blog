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
    return HttpResponse(str(num))