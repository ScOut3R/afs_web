from django.conf.urls import patterns


urlpatterns = patterns('',
	(r'^apply/', 'network.views.apply'),
)