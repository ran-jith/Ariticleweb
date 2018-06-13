from django.http import HttpResponse #respond to user via http (i think)
from django.shortcuts import render #to render a html template

#define 2 views that provided in urls.py(about and home)
def about(request):
    #return HttpResponse("about")#send something through HttpResponse
    return render(request,'about.html')

def homepage(request):
    #return HttpResponse("homepage")#function homepage from view will fire silmry above
    return render(request,'homepage.html')
