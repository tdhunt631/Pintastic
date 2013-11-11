from django.conf.urls import patterns, include, url
from pinboard import views

urlpatterns = patterns('',
	url(r'^$', views.Index.as_view(), name="index"),
	url(R'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
	url(R'^boards/$', views.Boards.as_view(), name="boards"),
	url(r'^board/(?P<pk>\d+)/$', views.Board_details.as_view(), name='board_details'),
	url(r'^pin/(?P<pk>\d+)/$', views.Pin_details.as_view(), name='pin_details'),
	url(r'^addPin/$', views.Add_pin.as_view(), name='add_pin'),
	url(r'^pinIt/(?P<pk>\d+)/$', views.Pin_it.as_view(), name='pin_it'),
	url(r'^addBoard/$', views.Add_board.as_view(), name='add_board'),
)
