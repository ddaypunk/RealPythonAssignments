from django.shortcuts import render
from django.template import Context, loader
from datetime import datetime
from django.http import HttpResponse

def index(request):
	return HttpResponse(
		"<html><body>Hello, World!</body></html>")

def about(request):
	return HttpResponse(
		"<html><body>Here is an about page. Want to return home?\
		<a href='/'>Back Home</a></body></html>")

def contact(request):
	return HttpResponse(
		"<html><body>Here is the contacts page.\
		Find out how to contact the developer.</body></html>")

def better(request):
	t = loader.get_template('betterhello.html')
	c = Context({'current_time': datetime.now(), })
	return HttpResponse(t.render(c))