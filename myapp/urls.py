
from django.conf.urls import url,include
from django.contrib import admin
from.import views                      #"from." means from current directory and need to import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^articles/',include('articles.urls')),#from app article urls.py file(this is how we include app url in main url)
    url(r'^about/$',views.about),         #about is the name of function created in views.py
    url(r'^$',views.homepage),            #home page goes to .com(main domain)

]

urlpatterns += staticfiles_urlpatterns() #this is for add styles,after creating this need to edit settings.py file
