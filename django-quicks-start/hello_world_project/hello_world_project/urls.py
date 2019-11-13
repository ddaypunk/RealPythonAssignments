from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns( 
	'',
	# Examples:
	# url(r'^$', 'hello_world_project.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^', include('hello_world.urls')),
	url(r'^about/', include('hello_world.urls')),
	url(r'^contact/', include('hello_world.urls')),
	url(r'^better/', include('hello_world.urls'))	)