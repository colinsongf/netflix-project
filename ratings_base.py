from collections import defaultdict
import netflix_objects as no

ratingsDictMovieID=defaultdict(list)
ratingsDictUserID=defaultdict(list)
ratingTuple=(ratingsDictMovieID,ratingsDictUserID)
def parse_ratings(): 
	global ratingsDictMovieID
	global ratingsDictUserID

	infile=open('u.data', 'r')
	content=infile.readlines()
	for line in content: 
		lineContent=line.split()
		userID=0
		movieID=0
		rating=0
		for index in lineContent:
			userID=lineContent[0]	
			movieID=lineContent[1]
			rating=lineContent[2]
		tempRating=no.rating(userID,movieID,rating)
		ratingsDictMovieID[int(tempRating.movieID)].append(tempRating)
		ratingsDictUserID[int(tempRating.userID)].append(tempRating)

	infile.close()	
	return ratingTuple

def read_out_ratings():
	global ratingsDictMovieID
	for k,v in ratingsDictMovieID.iteritems():
		for item in v: #returns every rating object in every list in ratings 
			print item.userID


read_out_ratings()