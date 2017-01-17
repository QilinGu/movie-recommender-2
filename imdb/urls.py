# app specific urls
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse


urlpatterns = patterns('',
    url(r'^home/$', 'imdb.views.home'),
    url(r'^add_user/$', 'imdb.views.add_user'),
    url(r'^list_all_users/$', 'imdb.views.list_all_users'),
	url(r'^add_movie/$', 'imdb.views.add_movie'),
	url(r'^rate_movie/$', 'imdb.views.rate_movie'),
	url(r'^list_all_movies/$', 'imdb.views.list_all_movies'),
	url(r'^get_reco/$', 'imdb.views.get_reco'),
	url(r'^about_dataset/$', 'imdb.views.about_dataset'),
	url(r'^contact_us/$', 'imdb.views.contact_us'),
        
    # ----------- Url matcher for views -------------------
    # home tab to others.
    url(r'^home/add_user/$', RedirectView.as_view(url='/imdb/add_user')),
    url(r'^home/list_all_users/$', RedirectView.as_view(url='/imdb/list_all_users')),
    url(r'^home/add_movie/$', RedirectView.as_view(url='/imdb/add_movie')),
    url(r'^home/rate_movie/$', RedirectView.as_view(url='/imdb/rate_movie')),
	url(r'^home/list_all_movies/$', RedirectView.as_view(url='/imdb/list_all_movies')),
	url(r'^home/get_reco/$', RedirectView.as_view(url='/imdb/get_reco')),
	url(r'^home/about_dataset/$', RedirectView.as_view(url='/imdb/about_dataset')),
	url(r'^home/contact_us/$', RedirectView.as_view(url='/imdb/contact_us')),

	# add_user tab to others.
    url(r'^add_user/home/$', RedirectView.as_view(url='/imdb/home')),
    url(r'^add_user/list_all_users/$', RedirectView.as_view(url='/imdb/list_all_users')),
    url(r'^add_user/add_movie/$', RedirectView.as_view(url='/imdb/add_movie')),
    url(r'^add_user/rate_movie/$', RedirectView.as_view(url='/imdb/rate_movie')),
	url(r'^add_user/list_all_movies/$', RedirectView.as_view(url='/imdb/list_all_movies')),
	url(r'^add_user/get_reco/$', RedirectView.as_view(url='/imdb/get_reco')),
	url(r'^add_user/about_dataset/$', RedirectView.as_view(url='/imdb/about_dataset')),
	url(r'^add_user/contact_us/$', RedirectView.as_view(url='/imdb/contact_us')),
	
	# list_all_users tab to others.
    url(r'^list_all_users/home/$', RedirectView.as_view(url='/imdb/home')),
    url(r'^list_all_users/add_user/$', RedirectView.as_view(url='/imdb/add_user')),
    url(r'^list_all_users/add_movie/$', RedirectView.as_view(url='/imdb/add_movie')),
    url(r'^list_all_users/rate_movie/$', RedirectView.as_view(url='/imdb/rate_movie')),
	url(r'^list_all_users/list_all_movies/$', RedirectView.as_view(url='/imdb/list_all_movies')),
	url(r'^list_all_users/get_reco/$', RedirectView.as_view(url='/imdb/get_reco')),
	url(r'^list_all_users/about_dataset/$', RedirectView.as_view(url='/imdb/about_dataset')),
	url(r'^list_all_users/contact_us/$', RedirectView.as_view(url='/imdb/contact_us')),

	# add_movie tab to others.
    url(r'^add_movie/home/$', RedirectView.as_view(url='/imdb/home')),
    url(r'^add_movie/add_user/$', RedirectView.as_view(url='/imdb/add_user')),
    url(r'^add_movie/list_all_users/$', RedirectView.as_view(url='/imdb/list_all_users')),
    url(r'^add_movie/rate_movie/$', RedirectView.as_view(url='/imdb/rate_movie')),
	url(r'^add_movie/list_all_movies/$', RedirectView.as_view(url='/imdb/list_all_movies')),
	url(r'^add_movie/get_reco/$', RedirectView.as_view(url='/imdb/get_reco')),
	url(r'^add_movie/about_dataset/$', RedirectView.as_view(url='/imdb/about_dataset')),
	url(r'^add_movie/contact_us/$', RedirectView.as_view(url='/imdb/contact_us')),

	# rate_movie tab to others.
    url(r'^rate_movie/home/$', RedirectView.as_view(url='/imdb/home')),
    url(r'^rate_movie/add_user/$', RedirectView.as_view(url='/imdb/add_user')),
    url(r'^rate_movie/list_all_users/$', RedirectView.as_view(url='/imdb/list_all_users')),
    url(r'^rate_movie/add_movie/$', RedirectView.as_view(url='/imdb/add_movie')),
	url(r'^rate_movie/list_all_movies/$', RedirectView.as_view(url='/imdb/list_all_movies')),
	url(r'^rate_movie/get_reco/$', RedirectView.as_view(url='/imdb/get_reco')),
	url(r'^rate_movie/about_dataset/$', RedirectView.as_view(url='/imdb/about_dataset')),
	url(r'^rate_movie/contact_us/$', RedirectView.as_view(url='/imdb/contact_us')),

	# list_all_movies tab to others.
    url(r'^list_all_movies/home/$', RedirectView.as_view(url='/imdb/home')),
    url(r'^list_all_movies/add_user/$', RedirectView.as_view(url='/imdb/add_user')),
    url(r'^list_all_movies/list_all_users/$', RedirectView.as_view(url='/imdb/list_all_users')),
    url(r'^list_all_movies/add_movie/$', RedirectView.as_view(url='/imdb/add_movie')),
	url(r'^list_all_movies/rate_movie/$', RedirectView.as_view(url='/imdb/rate_movie')),
	url(r'^list_all_movies/get_reco/$', RedirectView.as_view(url='/imdb/get_reco')),
	url(r'^list_all_movies/about_dataset/$', RedirectView.as_view(url='/imdb/about_dataset')),
	url(r'^list_all_movies/contact_us/$', RedirectView.as_view(url='/imdb/contact_us')),

	# get_reco tab to others.
    url(r'^get_reco/home/$', RedirectView.as_view(url='/imdb/home')),
    url(r'^get_reco/add_user/$', RedirectView.as_view(url='/imdb/add_user')),
    url(r'^get_reco/list_all_users/$', RedirectView.as_view(url='/imdb/list_all_users')),
    url(r'^get_reco/add_movie/$', RedirectView.as_view(url='/imdb/add_movie')),
	url(r'^get_reco/rate_movie/$', RedirectView.as_view(url='/imdb/rate_movie')),
	url(r'^get_reco/list_all_movies/$', RedirectView.as_view(url='/imdb/list_all_movies')),
	url(r'^get_reco/about_dataset/$', RedirectView.as_view(url='/imdb/about_dataset')),
	url(r'^get_reco/contact_us/$', RedirectView.as_view(url='/imdb/contact_us')),
	
	# about_dataset tab to others.
    url(r'^about_dataset/home/$', RedirectView.as_view(url='/imdb/home')),
    url(r'^about_dataset/add_user/$', RedirectView.as_view(url='/imdb/add_user')),
    url(r'^about_dataset/list_all_users/$', RedirectView.as_view(url='/imdb/list_all_users')),
    url(r'^about_dataset/add_movie/$', RedirectView.as_view(url='/imdb/add_movie')),
	url(r'^about_dataset/rate_movie/$', RedirectView.as_view(url='/imdb/rate_movie')),
	url(r'^about_dataset/list_all_movies/$', RedirectView.as_view(url='/imdb/list_all_movies')),
	url(r'^about_dataset/get_reco/$', RedirectView.as_view(url='/imdb/get_reco')),
	url(r'^about_dataset/contact_us/$', RedirectView.as_view(url='/imdb/contact_us')),

	# contact_us tab to others.
    url(r'^contact_us/home/$', RedirectView.as_view(url='/imdb/home')),
    url(r'^contact_us/add_user/$', RedirectView.as_view(url='/imdb/add_user')),
    url(r'^contact_us/list_all_users/$', RedirectView.as_view(url='/imdb/list_all_users')),
    url(r'^contact_us/add_movie/$', RedirectView.as_view(url='/imdb/add_movie')),
	url(r'^contact_us/rate_movie/$', RedirectView.as_view(url='/imdb/rate_movie')),
	url(r'^contact_us/list_all_movies/$', RedirectView.as_view(url='/imdb/list_all_movies')),
	url(r'^contact_us/get_reco/$', RedirectView.as_view(url='/imdb/get_reco')),
	url(r'^contact_us/about_dataset/$', RedirectView.as_view(url='/imdb/about_dataset')),


    # ----------- Url matcher for controller -------------------
    url(r'^add_user/addUserController/$', 'imdb.controller.addUser'),
	url(r'^add_movie/addMovieController/$', 'imdb.controller.addMovie'),
	
	url(r'^list_all_users/getAllUsers/$', 'imdb.controller.getAllUsers'),
	url(r'^list_all_movies/getAllMovies/$', 'imdb.controller.getAllMovies'),
	url(r'^get_reco/getRecommendations/$', 'imdb.controller.getRecommendations'),
	url(r'^rate_movie/rateMovieController/$', 'imdb.controller.rateMovie')
    
)

