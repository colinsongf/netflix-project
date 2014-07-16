import netflix_objects as no

def parse_moviebase():
	movie_dict=dict()
	with open('u.item') as infile:
		content = infile.readlines()
		for line in content: #each line contains data for a single movie
			pieces = line.split('|')
			pos=0
			movie_id=0
			movie_title=""
			movie_date=""
			movie_url=""
			genre_bitmap=[]
			for piece in pieces:
				if pos==0:
					movie_id=piece.strip()
				elif pos==1:
					movie_title=piece.strip()
				elif pos==2:
					movie_date=piece.strip()
				elif pos==3:
					pass
				elif pos==4:
					movie_url=piece.strip()
				elif pos > 4:
					genre_bitmap.append(int(piece.strip()))
				pos = pos + 1
			new_movie=no.movie(movie_id,movie_title,movie_date,movie_url,genre_bitmap)
			movie_dict[int(movie_id)]=new_movie
	return movie_dict


