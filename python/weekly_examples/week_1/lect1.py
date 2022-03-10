from turtle import hideturtle


print("Hello World")

# Datatypes
# Strings
# Integers
# Floats
# Booleans
# Tuples
# Lists
# Dictionaries

name = "Fred Flinstone"

print(name + ", my lucky number is " + "5") # cannot concatenate a string with an integer - must be the same data type

animals = ["Dolphin", "Penguin","Monkey"]
print(animals[1])
animals.append("Cheetah") ## append is the same as push in javascript
print(animals)


elon_musk = {
    "name": "Elon Musk",
    "is rich": True ## must be capitalized
}

sandwich = {
    'name': "peanut butter jelly sandwich",
    'is_spicy': False,
    'is_tasty': True
}
print(sandwich['name'])


if sandwich['is_spicy'] == True:
    print("Holy Moly it's Spicy!!")
else: 
    print('This ' + sandwich['name'] + ' tastes just right!')

    # print(f"This  + {sandwich['name']} +  tastes just right!") # need to have version 3 installed

for i in range(0, 5+1, 1):
    print(i)

animals = ["Dolphin", "Penguin","Monkey"]
for i in range(0,len(animals),1):
    print(animals[i])

def add_my_two_numbers(num_1,num_2):
    results = num_1 + num_2
    return results

print(add_my_two_numbers(7,3))


# f stirng

car = "black monte carlo"
car2 = "white porsche"

print(f"my car is a {car}, and hers is a {car2}")