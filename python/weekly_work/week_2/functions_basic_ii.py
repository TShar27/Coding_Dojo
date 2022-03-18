# 1
# Create a function that accepts a number as an input. 
# Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

def subtract_1(num):
    output = []
    for i in range(num,-1,-1):
        output.append(i)
    return output

print(subtract_1(5))


# 2
# Create a function that will receive a list with two numbers. 
# Print the first value and return the second.

# my way
def print_and_return(x,y):
    print(x)
    return(y)

print(print_and_return(1,2))

#dojo way
def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([1,2]))

# 3
# Create a function that accepts a list 
# and returns the sum of the first value in the list plus the list's length.

# my way 
def first_plus_length(list):
    sum = list[0] + len(list)
    return sum 

print(first_plus_length([1,2,3,4,5]))

# dojo way 
def first_plus_length(list):
    return list[0] + len(list)

print(first_plus_length([1,2,3,4,5]))

# 4
# Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False

def val_greater_than_second(list):
    if len(list) < 2:
        return False
    output = []
    for i in range(0,len(list)):
        if list[i] > list[1]:
            output.append(list[i])
    return output

print(val_greater_than_second([5,2,3,2,1,4]))
print(val_greater_than_second([3]))

# 5 
#  Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

def length_and_value(size,value):
     output= []
     for i in range(0,size):
        output.append(value)
     return output


print(length_and_value(10,4))
print(length_and_value(4,7))

