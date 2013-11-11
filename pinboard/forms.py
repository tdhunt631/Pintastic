from django.forms import ModelForm
from django import forms
from django.template import RequestContext

from pinboard.models import Pin, Comment, Board

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['comment']

class PinForm(ModelForm):
	class Meta:
		model = Pin
		fields = ['image', 'description', 'link', 'is_public', 'board']

class PiningForm(ModelForm):
	class Meta:
		model = Pin
		fields = ['board']

class BoardForm(ModelForm):
	class Meta:
		model = Board
		fields = ['name']
