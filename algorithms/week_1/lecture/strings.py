# create a function that returns true if a word is a palendron and false if it is not 
# When using a range loop the parameters are not inclusive 
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