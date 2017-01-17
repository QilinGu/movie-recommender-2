from __future__ import with_statement
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from math import sqrt

import collections
import MySQLdb
import json
import time

import time
import fileinput;

def addUser(request):
	print "inside controller"
	print "got response from add user form"
	if request.method == "POST":
		user_name = request.POST.get('name', '')
		user_age = request.POST.get('age', '')
		user_sex = request.POST.get('sex', '')
		user_occupation = request.POST.get('occupation', '')
		user_zipcode = request.POST.get('zipcode','')
	else:
		user_name = None
		user_age = None
		user_sex = None
		user_occupation = None
		user_zipcode = None
	
	mydb = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '', db = 'imdb')
	cursor = mydb.cursor()
	try:
		cursor.execute('INSERT INTO user(name, age, sex, occupation, zipcode) VALUES(%s, %s, %s, %s, %s)', 
						(user_name, int(user_age), user_sex, user_occupation, user_zipcode))
		status = 'success'
	except Error:
		status = 'failed'
		
	print status
	mydb.commit()
	cursor.close()
	return HttpResponse('{"status":"'+status+'"}', content_type='application/json')
#	return HttpResponse(request.META.get('HTTP_REFERER'))

def getAllUsers(request):
	print "getAllUsers called"
	mydb = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '', db = 'imdb')
	cursor = mydb.cursor()

	cursor.execute("SELECT COUNT(*) FROM user")
	result = cursor.fetchone()
	nrows = result[0]
	
	# Use all the SQL you like
	cursor.execute("SELECT * FROM user")
	objects_list = []
	
	# print all the first cell of all the rows
	outerObject = collections.OrderedDict()
	
	
	for row in cursor.fetchall() :
		innerObject = collections.OrderedDict()
		innerObject['id'] = row[0]
		innerObject['name'] = row[1]
		innerObject['age'] = row[2]
		innerObject['sex'] = row[3]
		innerObject['occupation'] = row[4]
		innerObject['zipcode'] = row[5]
		objects_list.append(innerObject)



	outerObject['data'] = objects_list
	outerObject['statusCode'] = 200
	outerObject['statusText'] = 'OK'
	outerObject['recordsTotal'] =  nrows
	outerObject['recordsFiltered'] = nrows
	finalJson = json.dumps(outerObject)

	mydb.commit()
	cursor.close()
	print "Done populating all users"
	
	#return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	return HttpResponse(finalJson, content_type='application/json')

def getAllMovies(request):
	print "getAllMovies called"
	finalJson = getAllMoviesData(request)
	print "Done populating all movies"
	return HttpResponse(finalJson, content_type='application/json')


def getAllMoviesData(request):
	mydb = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '', db = 'imdb')
	cursor = mydb.cursor()

	cursor.execute("SELECT COUNT(*) FROM movie")
	result = cursor.fetchone()
	nrows = result[0]
	
	# Use all the SQL you like
	cursor.execute("SELECT * FROM movie")
	objects_list = []
	
	# print all the first cell of all the rows
	outerObject = collections.OrderedDict()

	
	for row in cursor.fetchall():
		genreList = [];
		innerObject = collections.OrderedDict()
		innerObject['id'] = row[0]
		innerObject['title'] = row[1]
		innerObject['release_date'] = row[2]
		innerObject['video_release_date'] = row[3]
		innerObject['url'] = row[4]
		
		if int(row[5]) == 1:
			genreList.append('Unknown')
		if int(row[6]) == 1:
			genreList.append('Action')
		if int(row[7]) == 1:
			genreList.append('Adventure')
		if int(row[8]) == 1:
			genreList.append('Animation')
		if int(row[9]) == 1:
			genreList.append('Children')
		if int(row[10]) == 1:
			genreList.append('Comedy')
		if int(row[11]) == 1:
			genreList.append('Crime')
		if int(row[12]) == 1:
			genreList.append('Documentary')			
		if int(row[13]) == 1:
			genreList.append('Drama')			
		if int(row[14]) == 1:
			genreList.append('Fantasy')
		if int(row[15]) == 1:
			genreList.append('Film-Noir')
		if int(row[16]) == 1:
			genreList.append('Horror')
		if int(row[17]) == 1:
			genreList.append('Musical')
		if int(row[18]) == 1:
			genreList.append('Mystery')
		if int(row[19]) == 1:
			genreList.append('Romance')
		if int(row[20]) == 1:
			genreList.append('Sci-Fi')
		if int(row[21]) == 1:
			genreList.append('Thriller')
		if int(row[22]) == 1:
			genreList.append('War')
		if int(row[23]) == 1:
			genreList.append('Western')
			
		innerObject['genres'] = genreList		
		objects_list.append(innerObject)

	print innerObject
	
	outerObject['data'] = objects_list
	outerObject['statusCode'] = 200
	outerObject['statusText'] = 'OK'
	outerObject['recordsTotal'] =  nrows
	outerObject['recordsFiltered'] = nrows
	finalJson = json.dumps(outerObject)

	mydb.commit()
	cursor.close()
	
	return finalJson;
	
def addMovie(request):
	print "inside controller"
	print "got response from add movie form"
	if request.method == "POST":
		movie_title = request.POST.get('title', '')
		movie_release_date = request.POST.get('releaseDate', '')
		movie_video_release_date = request.POST.get('videoDate', '')
		movie_url = request.POST.get('url', '')
		movie_genre = request.POST.getlist('genre','')
	else:
		movie_title = None
		movie_release_date = None
		movie_video_release_date = None
		movie_url = None
		movie_genre = None
	
	print (movie_title, movie_release_date, movie_video_release_date, movie_url, movie_genre)

	mydb = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '', db = 'imdb')
	cursor = mydb.cursor()

	unknown = 1 if 'unknown' in movie_genre else 0
	action = 1 if 'action' in movie_genre else 0
	adventure = 1 if 'adventure' in movie_genre else 0
	animation = 1 if 'animation' in movie_genre else 0
	children = 1 if 'children' in movie_genre else 0
	comedy = 1 if 'comedy' in movie_genre else 0
	crime = 1 if 'crime' in movie_genre else 0
	documentary = 1 if 'documentary' in movie_genre else 0
	drama = 1 if 'drama' in movie_genre else 0
	fantasy = 1 if 'fantasy' in movie_genre else 0	
	film_noir = 1 if 'film_noir' in movie_genre else 0
	horror = 1 if 'horror' in movie_genre else 0
	musical = 1 if 'musical' in movie_genre else 0
	mystery = 1 if 'mystery' in movie_genre else 0
	romance = 1 if 'romance' in movie_genre else 0
	sci_fi = 1 if 'sci_fi' in movie_genre else 0
	thriller = 1 if 'thriller' in movie_genre else 0
	war = 1 if 'war' in movie_genre else 0
	western = 1 if 'western' in movie_genre else 0
		
	print (movie_title, movie_release_date, movie_video_release_date, movie_url, 
					unknown, action, adventure, animation, children, comedy, crime, documentary, drama,
					fantasy, film_noir, horror, musical, mystery, romance, sci_fi, thriller, war, western)
					
	cursor.execute('INSERT INTO movie(title, release_date, video_release_date, url, \
					unknown, action, adventure, animation, children, comedy, crime, documentary, \
					drama, fantasy, film_noir, horror, musical, mystery, romance, sci_fi, thriller, war, western) \
					VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', 
					(movie_title, movie_release_date, movie_video_release_date, movie_url, 
					unknown, action, adventure, animation, children, comedy, crime, documentary, drama,
					fantasy, film_noir, horror, musical, mystery, romance, sci_fi, thriller, war, western))
	
	mydb.commit()
	cursor.close()
	
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def rateMovie(request):
	print "inside rate movie logic."
	if request.method == "POST":
		userid = request.POST.get('userid', '')
		movieid = request.POST.get('movieid', '')
		rating = request.POST.get('rating', '')
	else:
		userid = None
		movieid = None
		rating = None

	userid = int(userid)
	movieid = int(movieid)
	rating = int(rating)

	print (userid, movieid, rating)

	mydb = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '', db = 'imdb')
	cursor = mydb.cursor()

	cursor.execute('SELECT * FROM rating WHERE user_id=%s AND movie_id=%s', (userid, movieid))
	result = cursor.fetchone()
	print result

	cursor = mydb.cursor()
	if not result:
		print "insert new rating"
		cursor.execute('INSERT INTO rating(rating, timestamp, user_id, movie_id) VALUES(%s, %s, %s, %s)',
					(rating, time.time(), userid, movieid))
	else:
		print "updating existing rating"
		cursor.execute('UPDATE rating SET rating=%s AND timestamp=%s WHERE user_id=%s AND movie_id=%s',
					   (rating, time.time(), userid, movieid))

	mydb.commit()
	cursor.close()

	print "completed rating movie."
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# Returns the Pearson correlation coefficient for p1 and p2
def sim_pearson(prefs, p1, p2):
    # Get the list of mutually rated items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]: si[item] = 1

    # if they are no ratings in common, return 0
    if len(si) == 0: return 0

    # Sum calculations
    n = len(si)

    # Sums of all the preferences
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    # Sums of the squares
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])

    # Sum of the products
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

    # Calculate r (Pearson score)
    num = pSum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0: return 0

    r = num / den

    return r

# Returns the best matches for person from the prefs dictionary.
# Number of results and similarity function are optional params.
def topMatches(prefs, person, n=5, similarity=sim_pearson):
    scores = [(similarity(prefs, person, other), other)
              for other in prefs if other != person]
    scores.sort()
    scores.reverse()
    return scores[0:n]


# Gets recommendations for a person by using a weighted average
# of every other user's rankings
def getUserBasedRecommendation(prefs, person, similarity=sim_pearson):
    totals = {}
    simSums = {}

    for other in prefs:

        # don't compare me to myself
        if other == person: continue

        # identify similar users using pearson correlation formula.
        sim = similarity(prefs, person, other)

        # ignore scores of zero or lower
        if sim <= 0: continue

        for item in prefs[other]:

            # only score movies I haven't seen yet
            if item not in prefs[person] or prefs[person][item] == 0:
                # Similarity * Score
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim

                # Sum of similarities
                simSums.setdefault(item, 0)
                simSums[item] += sim

    # Create the normalized list
    rankings = [(item, total / simSums[item]) for item, total in totals.items()]

    # Return the sorted list
    rankings.sort(key=extract_rating, reverse=True)
    return rankings

# Function to call for getting recommendations.
def getRecommendations(request):
	print "inside recommendations controller"

	if request.method == "POST":
		user_id = request.POST.get('userid', '1')
		nmovies = request.POST.get('nmovies', '10')
		recoType = request.POST.get('recoType', 'I')
	else:
		user_id = None
		nmovies = None
		recoType = None

	prefs = loadMovieLens()

	print (user_id, nmovies, recoType)
		
	nmovies = int(nmovies)
	user_id = int(user_id)
	if recoType == "I":
		print "computing item based recommendation"
		itemsim = calculateSimilarItems(prefs, n=50)
		rankings = getRecommendedItems(prefs,itemsim, user_id)	
	elif recoType == "U":
		print "computing user based recommendation"
		rankings = getUserBasedRecommendation(prefs,user_id)

	finalJson = json.dumps(rankings[0:nmovies])
	print finalJson

	return HttpResponse(finalJson, content_type='application/json')

def transformPrefs(prefs):
    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})

            # Flip item and person
            result[item][person] = prefs[person][item]
    return result


def calculateSimilarItems(prefs, n=10):
    # Create a dictionary of items showing which other items they
    # are most similar to.
    result = {}
    # Invert the preference matrix to be item-centric
    itemPrefs = transformPrefs(prefs)
    c = 0
    for item in itemPrefs:
        # Status updates for large datasets
        c += 1
        if c % 100 == 0: print "%d / %d" % (c, len(itemPrefs))
        # Find the most similar items to this one
        scores = topMatches(itemPrefs, item, n=n, similarity=sim_distance)
        result[item] = scores
    return result


def getRecommendedItems(prefs, itemMatch, user):
    userRatings = prefs[user]
    scores = {}
    totalSim = {}
    # Loop over items rated by this user
    for (item, rating) in userRatings.items():

        # Loop over items similar to this one
        for (similarity, item2) in itemMatch[item]:

            # Ignore if this user has already rated this item
            if item2 in userRatings: continue
            # Weighted sum of rating times similarity
            scores.setdefault(item2, 0)
            scores[item2] += similarity * rating
            # Sum of all the similarities
            totalSim.setdefault(item2, 0)
            totalSim[item2] += similarity

    # Divide each total score by total weighting to get an average
    #    rankings = [(item, score / totalSim[item]) for item, score in scores.items()]
    recoObject = []
    rankings = []
    for item, score in scores.items():
    	recoObject = [item, score/totalSim[item]]
    	rankings.append(recoObject)

    rankings.sort(key=extract_rating, reverse=True)
    return rankings

def extract_rating(json):
	try:
		return float(json[1])
	except KeyError:
		print "some error in extract_rating(json)"
	
	return 0

def loadMovieLens():
	# Get movie titles
	print "inside load movie lens"
	movies = {}
	mydb = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '', db = 'imdb')
	cursor = mydb.cursor()

	cursor.execute("SELECT id, title FROM movie")
	for row in cursor.fetchall():
		movie_id = int(row[0])
		movie_title = row[1]
		
		#print (movie_id, movie_title)
		movies[movie_id] = movie_title

	prefs = {}
	cursor = mydb.cursor()
	cursor.execute("SELECT * FROM rating")
	
	for row in cursor.fetchall():
		user_id = int(row[2])
		movie_id = int(row[3])
		rating = int(row[0])
		
		#print (user_id, movie_id, rating)
		prefs.setdefault(user_id, {})
		prefs[user_id][movies[movie_id]] = float(rating)
		
	mydb.commit()
	cursor.close()
	
	return prefs

# Returns a distance-based similarity score for person1 and person2
def sim_distance(prefs, person1, person2):
    # Get the list of shared_items
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]: si[item] = 1

    # if they have no ratings in common, return 0
    if len(si) == 0: return 0

    # Add up the squares of all the differences
    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2)
                          for item in prefs[person1] if item in prefs[person2]])

    return 1 / (1 + sum_of_squares)
