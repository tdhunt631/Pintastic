from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.views.generic.edit import FormMixin
from endless_pagination.views import AjaxListView
from pinboard.models import Comment, Board, Pin
from pinboard.forms import *

#adds ability to decorate a class
def class_view_decorator(decorator):
	def my_decorator(View):
		View.dispatch = method_decorator(decorator)(View.dispatch)
		return View
	return my_decorator

class Index(AjaxListView):
	template_name = 'pinboard/index.html'
	page_template = 'pinboard/pin_list.html'
	model = Pin
	context_object_name = 'pins'
	paginate_by = 5	

	def get_queryset(self):
		return Pin.objects.filter(is_public=True).order_by('-pub_date')

@class_view_decorator(login_required)
class Boards(ListView):
	model = Board 
	context_object_name = 'boards'

	def get_queryset(self):
		return Board.objects.filter(created_by = self.request.user.id)

class Board_details(AjaxListView):
	template_name = 'pinboard/board_details.html'
	page_template = 'pinboard/pin_list.html'
	model = Pin
	context_object_name = 'pins'
	paginate_by = 5

	def get_queryset(self):
		return Pin.objects.filter(is_public=True).filter(board__in=self.kwargs['pk']).order_by('-pub_date')

@class_view_decorator(login_required)
class Add_board(CreateView):
	form_class = BoardForm
	template_name = 'pinboard/add_board.html'

	def get_form(self, form_class):
		if self.request.user.is_authenticated():
			form = super(Add_board, self).get_form(form_class)
			form.instance.created_by = self.request.user
			return form

	def get_success_url(self):
		return reverse('pinboard:index')

class Pin_details(CreateView):
	form_class = CommentForm
	template_name = 'pinboard/pin_details.html'

	def get_context_data(self, **kwargs):
		context = super(Pin_details, self).get_context_data(**kwargs)
		currentPin = get_object_or_404(Pin, id=self.kwargs['pk'])
		context['comments'] = Comment.objects.filter(pin = currentPin)
		context['pin'] = get_object_or_404(Pin, id=self.kwargs['pk'])
		return context

	def get_form(self, form_class):
		if self.request.user.is_authenticated():
			form = super(Pin_details, self).get_form(form_class)
			form.instance.user = self.request.user
			form.instance.pin = get_object_or_404(Pin, id=self.kwargs['pk'])
			return form 

	def get_success_url(self):
		return reverse('pinboard:pin_details', args=[str(self.kwargs['pk'])])

@class_view_decorator(login_required)
class Add_pin(CreateView):
	form_class = PinForm
	template_name = 'pinboard/add_pin.html'

	def get_form(self, form_class):
		if self.request.user.is_authenticated():
			form = super(Add_pin, self).get_form(form_class)
			form.instance.created_by = self.request.user
			form.fields['board'].queryset = Board.objects.filter(created_by = self.request.user)
			return form

	def get_success_url(self):
		return reverse('pinboard:index')

@class_view_decorator(login_required)
class Pin_it(UpdateView):
	model  = Pin
	form_class = PiningForm
	fields = ['board']
	template_name = 'pinboard/pinit.html'
	success_url = '/'
	
	def get_form(self, form_class):
		form = super(Pin_it, self).get_form(form_class)
		form.fields['board'].queryset = Board.objects.filter(created_by = self.request.user)
		return form
		
	def get_object(self, queryset=None):
		return get_object_or_404(Pin, id=self.kwargs['pk'])
