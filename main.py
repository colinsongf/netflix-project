import movie_base
import ratings_base
import user_base
import netflix_objects
import heapq
import random
from random import randint

movieBase=movie_base.parse_moviebase()
ratingBaseMovieID=ratings_base.parse_ratings()[0]
ratingsBaseUserID=ratings_base.parse_ratings()[1]
userBase=user_base.parse_users()


def compute_rm_all():
	global movieBase
	global ratingBaseMovieID
	for k,v in movieBase.items():
		v.compute_rm(movieBase,ratingBaseMovieID)
	return movieBase

def compute_ug_all():
	global movieBase
	global ratingsBaseUserID
	for k,v in userBase.items():
		v.compute_ug(movieBase,ratingsBaseUserID)
	return userBase
def compute_pug_all():
	global ratingBaseUserID
	userBase=compute_ug_all()
	movieBase=compute_rm_all()
	for k,v in userBase.items():
		v.compute_pug(movieBase,ratingsBaseUserID)
	return userBase
def compute_topk_all(k):
	userDict = compute_pug_all()
	movieDict=compute_rm_all()

	for userID, user in userDict.items():
		topMovieList=[]
		topMovieDict=dict()
		topSorted=[]
		for movieID, movie in movieDict.items():
			weightedRatings=[]
			for x in range(0,18):
				if movie.genre[x]==1:
					weightedRatings.append(movie.r_m*user.pug[x])
			if len(weightedRatings) > 0:
				maxRating=max(weightedRatings)
			topMovieDict[maxRating]=movieDict[movieID] # rating = key, movie object = val
														# easier to sort keys than to sort values
		topSorted=heapq.nlargest(k, topMovieDict) #get top k weighted ratings
		for weightedRating in topSorted:
			user.top_k.append((topMovieDict[weightedRating],weightedRating)) 
	return userDict
def print_topk_all(j,n,k): # j = total number of users, n = number of users we want top list from, k = number of top movies in top movie list
	userDict=compute_topk_all(k)
	movieDict=compute_rm_all()
	randUsers = []
	for x in range(1,n):
		currUserID=randint(1,j)
	 	currUser=userDict[currUserID]
		topK=currUser.top_k
		print "======================"
		print "user", currUserID
		print "======================"
		topMoviePos=1 #
		for movieTup in topK:
			print "------------------"
			currMovie=movieTup[0]
			currRating=movieTup[1]
			print "#",topMoviePos,"top movie for this user"
			print "Movie's weighted rating for user:", currRating
			currMovie.str()
			print "------------------"
			topMoviePos=topMoviePos+1
print_topk_all(943,3,50)

'''
unknown|0
Action|1
Adventure|2
Animation|3
Children's|4
Comedy|5
Crime|6
Documentary|7
Drama|8
Fantasy|9
Film-Noir|10
Horror|11
Musical|12
Mystery|13
Romance|14
Sci-Fi|15
Thriller|16
War|17
Western|18
'''