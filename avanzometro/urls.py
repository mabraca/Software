from django.conf.urls import url, include
from django.contrib import admin
from .views import home, register, index_page
urlpatterns = [
    url(r'^$', home),
    url(r'^login/', register),
    url(r'^index/', index_page),
]