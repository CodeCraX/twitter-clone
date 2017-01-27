from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Tweet
from . import serializers
from .permissions import IsOwnerOrReadOnly


class TweetList(generics.ListCreateAPIView):
    """List of all tweets"""
    queryset = Tweet.objects.all()
    serializer_class = serializers.TweetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    #creating a new tweet by respective owner
    def perform_create(self, serializer):           
        serializer.save(owner=self.request.user)


class TweetDetail(generics.RetrieveDestroyAPIView):
    """Retieve or Delete a tweet"""

    queryset = Tweet.objects.all()
    serializer_class = serializers.TweetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)



class UserList(generics.ListAPIView):
    """List of all Users"""
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """Retrive a User"""

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
   return Response({
       'users': reverse('user-list', request=request, format=format),
       'tweets-list': reverse('tweet-list', request=request, format=format)
       
   })

