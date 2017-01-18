from django.db import models

# Create your models here.

class Tweet(models.Model):
	owner = models.ForeignKey('auth.User', related_name='tweets')
	created = models.DateTimeField(auto_now_add=True)
	text = models.CharField(max_length=140, blank=False)
	liked_by = models.ManyToManyField('auth.User', related_name='likes')

	class Meta:
		ordering = ('created',)


		sadlkfsladkjf