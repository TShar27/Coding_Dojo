# create a function that returns true if a word is a palendron and false if it is not 
# When using a range loop the parameters are not inclusive 
import numbers
from numpy import number
from pyparsing import Or


def is_palindrone(input):
    reverse_input = ""
    for i in range(len(input)-1,-1,-1):
        reverse_input += input[i].lower()
    # if reverse_input ==input:
    #     return True
    # return False
    return reverse_input == input.lower() # the comparison of a conditonal will be True or False

print(is_palindrone("Racecar"))
print(is_palindrone("turtle"))
print(is_palindrone("ANutForaJarofTuna"))


# Create a function that, given a string, returns all of that string’s contents, but without blanks. 
# If given the string " Pl ayTha tF u nkyM usi c ", return "PlayThatFunkyMusic".

def remove_space(input):
    return input.replace(" ","")

input = " Pl ayTha tF u nkyM usi c "
print(remove_space(input))

# OR

def remove(string):
    return "".join(string.split())
     
string = " Pl ayTha tF u nkyM usi c "
print(remove(string))



# Create a function that given a string, returns the integer made from the string’s digits. 
# Given "0s1a3y5w7h9a2t4?6!8?0", the function should return the number 1357924680.


# GOT IT
def ExtractDigitfromString(string):
    leng = []
    for i in range(len(string)):
        if (string[i]).isdigit():
            leng.append(string[i])
    return ''.join(leng)
string = '0s1a3y5w7h9a2t4?6!8?0'
print(ExtractDigitfromString(string))


#regex way

import re
 
# initializing string
test_string = '0s1a3y5w7h9a2t4?6!8?0'
 
# printing original strings 
print("The original string : " + test_string)
 
# using re
# Extract digit string
res = re.sub("\D", "", test_string)
     
# print result
print("The digits string is : " + str(res))


# Create a function that, given a string, returns the string’s acronym (first letters only, capitalized). 
#Given " there's no free lunch - gotta pay yer way. ", return "TNFL-GPYW". 
#Given "Live from New York, it's Saturday Night!", return "LFNYISN".

#FINALLY
def acronym(string):
    new_string = string.split()
    new_str = []
    print(new_string)
    for word in new_string:
        new_str.append(word[0])
    final = ''.join(new_str)
    return(final.upper())

string = "there's no free lunch - gotta pay yer way."
string = "Live from New York, it's Saturday Night!"
print(acronym(string))















