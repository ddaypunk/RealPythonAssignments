from django.conf.urls import patterns, url
from blongo_app import views

urlpatterns = patterns('blongo_app.views',
	url(r'^$', views.index, name='index'),
	)