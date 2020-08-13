from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^$',views.diariesView, name='diariesView'),
    url(r'^(?P<diaryName>[\w]+)/$', views.photosView, name="photosView"),
    url(r'^(?P<diaryName>[\w]+)/upload/$', views.uploadPhoto, name="uploadPhoto"),
    url(r'^(?P<diaryName>[\w]+)/post/(?P<photoTitle>[\w]+)/$', views.postComment, name="postComment")
]
