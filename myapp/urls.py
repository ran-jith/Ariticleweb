
from django.conf.urls import url,include
from django.contrib import admin
from.import views                      #"from." means from current directory and need to import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as art_views #there a 2 views present here thats why

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^articles/',include('articles.urls')),#from app article urls.py file(this is how we include app url in main url)
    url(r'^accounts/',include('accounts.urls')),
    url(r'^about/$',views.about),         #about is the name of function created in views.py
    url(r'^$',art_views.article_list,name="home"),            #home page goes to .com(main domain)

]
#for image
urlpatterns += staticfiles_urlpatterns() #this is for add styles,after creating this need to edit settings.py file

#for media
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
