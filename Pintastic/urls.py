from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^', include('pinboard.urls', namespace="pinboard")),
	url(r'^users/', RedirectView.as_view(url='/')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/', include('registration.backends.simple.urls')),	
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
