from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Tweet

class TweetSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	
	class Meta:
		model = Tweet
		fields = ('id', 'owner', 'created', 'tweet', 'liked_by')

class UserSerializer(serializers.ModelSerializer):
	tweets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model = User
		fields = ('url', 'username', 'tweets', 'likes')