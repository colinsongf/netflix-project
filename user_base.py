import netflix_objects as no

userBase = dict()

def parse_users():
	file=open('u.user','r')
	content = file.readlines()
	for line in content:
		piece = line.split('|')
		ID = piece[0]
		age=piece[1]
		gender=piece[2]
		occupation=piece[3]
		ZIP=piece[4]
		new_user = no.user(ID,age,gender,occupation,ZIP)
		userBase[int(ID)]=new_user
	file.close()
	return userBase