from django.forms import ModelForm
from django import forms

from pinboard.models import Pin, Comment, Board

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['comment']
