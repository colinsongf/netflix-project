import numpy as np
import sys
from collections import defaultdict

class movie:
	def __init__(self, myID, myTitle, myDate, myURL, myGenre):
		self.ID=myID
		self.title=myTitle
		self.date=myDate
		self.genre=myGenre
		self.URL=myURL
		self.r_m=0
	def compute_rm(self,movieDict, ratingDict):
		temp_list=ratingDict[int(self.ID)]
		ratings_sum=sum(int(rating_object.rating) for rating_object in temp_list)
		ratingsc=len(temp_list)
		self.r_m = (float(ratings_sum)/float(ratingsc))
	def str(self):
		print "Title: ",self.title
		print "Movie ID: ", self.ID
		print "Date: ",self.date
		print "IMDB URL: " + self.URL
		print "Average star rating by all users:",self.r_m

	def calculate_rm(self,ratings):
		myRatings = ratings[self.ID] # list of ratings objects
		numberOfRatings=len(myRatings)
		sumOfRatings=sum(ratingObj.rating for ratingObj in myRatings)
		self.r_m=float(sumOfRatings)/float(numberOfRatings)
class rating:
	def __init__(self,myUserID,myMovieID,myRating):
		self.userID=myUserID
		self.movieID=myMovieID
		self.rating=myRating
class user: 
	def __init__(self,myID,myAge,myGender,myOccupation,myZIP):
		self.ID=myID
		self.age = myAge
		self.gender = myGender
		self.occupation = myOccupation
		self.ZIP = myZIP
		self.ug=[]
		self.pug=[]
		self.top_k=[]
		for x in range(0,18):
			self.ug.append(0)
		self.pug=[]
		for x in range(0,18):
			self.pug.append(0)
		self.top_k=[]
	def compute_ug(self,movieDict,ratingDictUserID):
		myRatings=ratingDictUserID[int(self.ID)]
		tempRatingList=defaultdict(list)
		for review in myRatings:
			curr_movie = movieDict[int(review.movieID)]
			for x in range(0,18):
				if curr_movie.genre[x]==1:
					tempRatingList[x].append(int(review.rating))

		for k,v in tempRatingList.items():
			sumOfReviews=sum(v)
			numberOfReviews=len(v)
			self.ug[k]=float(sumOfReviews)/float(numberOfReviews)	


	def compute_pug(self,movieDict, ratingDictUserID):
		myRatings=ratingDictUserID[int(self.ID)]
		averageGenreRating=defaultdict(list)
		tempList=[]
		for x in range (0,18):
			tempList.append(0)
		for review in myRatings:
			curr_movie=movieDict[int(review.movieID)]
			for x in range(0,18):
				if curr_movie.genre[x]==1:
					averageGenreRating[x].append(curr_movie.r_m)
		for x in range(0,18):
			rsum=0
			if len(averageGenreRating[x])>0:
				for rating in averageGenreRating[x]:
					rsum = rsum + rating
			if len(averageGenreRating[x]) > 0: 
				tempList[x]=rsum/len(averageGenreRating[x])
		for x in range(0,18):
			if tempList[x]>0:
				self.pug[x]=float(self.ug[x])/float(tempList[x])





