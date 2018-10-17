# all urls listed here will start with at least mysite.com/blog/

from django.urls import path
from blog import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
]