# #How do we build a function
# def car_info(make,model,year=2020):
#      print(make)
#      print(model)
#      print(year)
#      return f"I like {make} {model} from the year {year}"

# #car_info("Golf GTI","Volkswagon", year = 2021)

# #print(car_info("Golf GTI","Volkswagon", year = 2021))

# car1= car_info("Golf GTI","Volkswagon", year = 2021)
# print(car1)

# #example 2 - random
# import random 


# print(round(random.random()*50))
# import random 
 
#  #example 3 - even, odd function
# def amount_to_be_added():
#     amount = round(random.random()*100)

#     if amount % 2 == 0:
#         print(f"{amount} is even")
#     else:
#         print(f"{amount} is odd")
#     return amount

# print(amount_to_be_added())

# Dictionaries

sports_cars = {
    'Chevrolet': 'Corvette', # 'Key':'Value'
    'Nissan': 'GTR',
    'Ford': 'GT'
}

print(sports_cars)
print(sports_cars['Nissan'])
print(sports_cars['GTR']) # Cannot call 'Key'

# adding a value to dictionary
sports_cars['Toyota']="Supra"

print(sports_cars)

# for loops 
for car in sports_cars:
    print(car) # will give us keys 
    print(sports_cars[car]) # will give us values 

# .keys()
for car in sports_cars.keys():
    print(car)

# .values()
for car in sports_cars.values():
     print(car)

# .items() - Prints both key and value. Can name the variables anything you want 
for key,val in sports_cars.items():
    print(key,val) 