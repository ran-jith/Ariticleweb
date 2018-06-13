
from django.shortcuts import render
from .models import Article #import table(or class) to display
from django.http import HttpResponse
#in html art,in dictionary article in general articles

def article_list(request): #for /articles/
    articles = Article.objects.all().order_by('date')
    return render(request,'articles/article_list.html',{ 'article':articles })#render(request(always),path)#last create a dictionary to send data to templates

def article_detail(request,slug): #for /slug/ and we capture variable 'slug' in urls.py,this slug is not db slug directly
    #return HttpResponse(slug)

    arts = Article.objects.get(slug=slug)
    return render(request,'articles/article_detail.html',{ 'artd':arts })
