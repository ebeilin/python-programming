#declare an empty list
classmates = [] 

#add items to list 
classmates.append('Sue')
classmates.append('Shad')
classmates.append('Eva')
classmates.append('Mayank')
classmates.append('Chin')
classmates.append('Gus')
classmates.append('Jeremy')
classmates.append('Dan')
classmates.append('Julian')
classmates.append('Aaron')

#access an item at a specific position
print(classmates[0])
print(classmates[4]) #fifth element

#get the size of the list
print(len(classmates))

#remove an item from end of list
classmates.pop()

#insert at specific position
classmates.insert(0,'Aaron')

print(classmates)

#removing an item from the list
classmates.remove('Gus')

print(classmates)

#edit an item in the list
classmates[1] = 'Sue Work'

print(classmates)

#iterate over a list(search for element)
for classmate in classmates:
    if(classmate == 'Gus'): 
        print('Great, Gus is in the class!')

'''
#edit elements while iterating
for index, classmate in enumerate(classmates):
    classmates[index] += '- Python Student'
'''

'''
#change names to uppercase
for index, classmate in enumerate(classmates):
    #classmates[index] = classmate.upper()
    classmates[index] = classmates[index].upper()

print(classmates)
'''

#create a list of all the marvel movies Iron man to End Game

#go through the list and create a second list with all the titles that have 'The
#in their names 

marvel_movies = ['Iron Man', 'The Incredible Hulk', 'Iron Man 2', 'Thor', 'Captain America: The First Avenger', 'The Avengers / Avengers Assemble', 'Iron Man 3', 'Thor: The Dark World', 'Captain America: The Winter Soldier', 'Guardians of the Galaxy', 'Avengers: Age of Ultron', 'Ant Man', 'Captain America: Civil War', 'Doctor Strange', 'Guardians of the Galaxy 2', 'Spiderman: Homecoming', 'Thor: Ragnarok', 'Black Panther', 'Avengers: Infinity War', 'Antman and the Wasp', 'Captain Marvel', 'Avengers: Endgame']
newmovie = []

for index, movie in enumerate(marvel_movies):
    if 'the ' in movie.lower():
        newmovie.append(movie)

print(newmovie)



#escaping an apostrophe
#'Marvel\'s The Avengers'













