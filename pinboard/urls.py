from django.conf.urls import patterns, include, url
from pinboard import views

urlpatterns = patterns('',
	url(r'^$', views.Index.as_view(), name="index"),
	url(R'^boards/$', views.Boards.as_view(), name="boards"),
	url(r'^board/(?P<pk>\d+)/$', views.Board_details.as_view(), name='board_details'),
)
