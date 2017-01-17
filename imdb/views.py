from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
	print "home page loaded"
	return render_to_response('home.html', context_instance=RequestContext(request))

def add_user(request):
	print "add_user page loaded"
	return render_to_response('add_user.html', context_instance=RequestContext(request))
	
def list_all_users(request):
	print "list_all_users page loaded"
	return render_to_response('list_all_users.html', context_instance=RequestContext(request))
	
def add_movie(request):
	print "add_movie page loaded"
	return render_to_response('add_movie.html', context_instance=RequestContext(request))
	
def rate_movie(request):
	print "rate_movie page loaded"
	return render_to_response('rate_movie.html', context_instance=RequestContext(request))
	
def list_all_movies(request):
	print "list_all_movies page loaded"
	return render_to_response('list_all_movies.html', context_instance=RequestContext(request))
	
def get_reco(request):
	print "get_reco page loaded"
	return render_to_response('get_reco.html', context_instance=RequestContext(request))
	
def about_dataset(request):
	print "about_dataset page loaded"
	return render_to_response('about_dataset.html', context_instance=RequestContext(request))

def contact_us(request):
	print "contact_us page loaded"
	return render_to_response('contact_us.html', context_instance=RequestContext(request))
