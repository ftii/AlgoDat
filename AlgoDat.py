import csv
class User(object):
	name = ""
	surname = ""
	email = ""
	location = ""
	def __init__(self, name, surname, email, location):
		self.name = name
		self.surname = surname
		self.email = email
		self.location =location
def make_user(name,surname,email,location):
	user= User(name,surname,email,location)
	return user

def sort(array):
	less = []
	equal = []
	greater = []

	if len(array) > 1:
		pivot = array[0].name
		for x in array:
			if x.name < pivot:
				less.append(x)
			if x.name == pivot:
				equal.append(x)
			if x.name > pivot:
				greater.append(x)
		return sort(less)+equal+sort(greater)
	else: 
		return array

array=[]
with open('Data.csv', newline='') as csvfile:
	data = csv.reader(csvfile)
	for row in data:
		array.append(make_user(row[1],row[2],row[0],row[9]))
print(array[0].name)
sort(array)	
