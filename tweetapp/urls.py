from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import routers



urlpatterns = [
	url(r'^$', views.api_root),
    url(r'^tweets/$', views.TweetList.as_view(), name='tweet-list'),
    url(r'^tweets/(?P<pk>[0-9]+)/$', views.TweetDetail.as_view(), name='tweet-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)