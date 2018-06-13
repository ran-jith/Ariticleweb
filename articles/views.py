
from django.shortcuts import render,redirect
from .models import Article #import table(or class) to display
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms
#in html art,in dictionary article in general articles

def article_list(request): #for /articles/
    articles = Article.objects.all().order_by('date')
    return render(request,'articles/article_list.html',{ 'article':articles })#render(request(always),path)#last create a dictionary to send data to templates

def article_detail(request,slug): #for /slug/ and we capture variable 'slug' in urls.py,this slug is not db slug directly
    #return HttpResponse(slug)

    arts = Article.objects.get(slug=slug)
    return render(request,'articles/article_detail.html',{ 'artd':arts })

@login_required(login_url="/accounts/login") #if user not loged in it blocks create option and redirect to login page
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            #save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
        return render(request,'articles/article_create.html',{'form':form})
