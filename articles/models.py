from django.db import models
from django.contrib.auth.models import User

"""
when we make any changes in models need to execute the following commands
==>python manage.py makemigrations
==>python manage.py migrate
"""
#models in python are class which represents a table in database
#each model maps to a single table in database

class Article(models.Model): #syntax in django
#title,slug etc are represents columns in table Article
    title = models.CharField(max_length=100)
    slug = models.SlugField() #slugs are used later for url names
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.jpeg', blank=True)
    author = models.ForeignKey(User,default=None)

    def __str__(self):  #for the purpose of shell(it is like inbuit fn)
        return self.title

    def snippet(self):  #for displaying some limited characters in size
        return self.body[:50] + '...etc' #after 50 characters it displays '...etc'
