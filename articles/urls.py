
from django.conf.urls import url
from.import views                      #"from." means from current directory and need to import views

app_name = 'articles' #for identify ulr names in different apps

urlpatterns = [
    url(r'^$',views.article_list, name="list"), #we can simply name anything to the url ,may use the
    url(r'^(?P<slug>[\w-]+)/$',views.article_detail, name="detail"),   #this slug is send to views.py(in fn article_detail) ,slug is the variable name here that take input from [w.blah blah]

]
