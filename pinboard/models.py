from django.db import models
from django.contrib.auth.models import User

class Pin(models.Model):
	image = models.ImageField(upload_to='uploads/%Y/%m/%d/')
	description = models.TextField()
	created_by = models.ForeignKey(User)
	pub_date = models.DateTimeField(auto_now_add=True)
	link = models.URLField(null=True, blank=True)
	is_public = models.BooleanField(default=True)
	board = models.ManyToManyField('Board')

	def __unicode__(self):
		return self.image.url

class Comment(models.Model):
	user = models.ForeignKey(User)
	pin = models.ForeignKey(Pin)
	comment = models.TextField()

	def __unicode__(self):
		return self.comment

class Board(models.Model):
	created_by = models.ForeignKey(User)
	name = models.CharField(max_length=60)
	
	def __unicode__(self):
		return self.name
