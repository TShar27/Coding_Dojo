# #How do we build a function
def car_info(make,model,year=2020):
     print(make)
     print(model)
     print(year)
     return f"I like {make} {model} from the year {year}"

#car_info("Golf GTI","Volkswagon", year = 2021)

#print(car_info("Golf GTI","Volkswagon", year = 2021))

car1= car_info("Golf GTI","Volkswagon", year = 2021)
print(car1)

# #example 2 - random
import random 


print(round(random.random()*50))
import random 
 
#  #example 3 - even, odd function
def amount_to_be_added():
    amount = round(random.random()*100)

    if amount % 2 == 0:
        print(f"{amount} is even")
    else:
        print(f"{amount} is odd")
    return amount

print(amount_to_be_added())

# Dictionaries

sports_cars = {
    'Chevrolet': 'Corvette', # 'Key':'Value'
    'Nissan': 'GTR',
    'Ford': 'GT'
}

print(sports_cars)
print(sports_cars['Nissan'])
print(sports_cars['GTR']) # Cannot call 'Key'

# # adding a value to dictionary
sports_cars['Toyota']="Supra"

print(sports_cars)

# # for loops 
for car in sports_cars:
    print(car) # will give us keys 
    print(sports_cars[car]) # will give us values 

# # .keys()
for car in sports_cars.keys():
    print(car)

# # .values()
for car in sports_cars.values():
     print(car)

# # .items() - Prints both key and value. Can name the variables anything you want 
for key,val in sports_cars.items():
    print(key,val) 

# create a function that adds a genre and list of artists onto our dictionary def add_genre_and_artists(genre,artists)
from pickle import APPEND


artists = {
    'hip-hop': ['eminem','jay-z','snoop-dog'],
    'rap': ['50 cent','dr. dre','j-cole'],
    'country':  ['tim mcgraw','jason aldean','eric church'],
}

def add_genre_and_artist(genre,artist_list):
    artists[genre] = artist_list
    return artists

print(add_genre_and_artist("pop",['bruno mars','the weeknd','justin beiber']))
print(add_genre_and_artist("haus",['black loops','shar bros','saison']))       

# create a function that adds to the correct genre
def add_to_genre(genre, artist_list):
    if genre in artists:
        # artists[genre].append(artist_list) # if we didnt use the for loop, the values in the fuction would still be added to the dictionary but they would be added outside of the country list, It would create a separate list added to the end of all the values
        for artist in artist_list:
            print(artist)
            artists[genre].append(artist)
    return artists

print(add_to_genre('country',['luke combs','kane brown','darius rucker']))