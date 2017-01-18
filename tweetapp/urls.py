from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^tweets/$', views.TweetList.as_view(), name='snippet-list'),
    url(r'^tweets/(?P<pk>[0-9]+)/$', views.TweetDetail.as_view(), name='snippet-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    # url(r'^users/register', 'tweetapp.views.create_auth'),
]

urlpatterns = format_suffix_patterns(urlpatterns)