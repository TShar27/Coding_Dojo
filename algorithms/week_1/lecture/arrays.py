# shuffling the numbers inside an array
import random
def shuffle(arr):
    new_arr = []
    for i in range(len(arr)):
    # while len(arr) != 0: ACan use a while loop to solve this problem too
        random_index = random.randint(0,len(arr)-1)
        new_arr.append(arr[random_index])
        arr.pop(random_index)
    return new_arr

print(shuffle([43,21,78,9,7,2])) # shuffle this 


#skyline heights

def skyline(arr):
    new_arr = []
    last_tallest = 0 
    for i in range(len(arr)):
        if arr[i] >0 and arr[i] > last_tallest:
            new_arr.append(arr[i])
            last_tallest = arr[i]
    print(new_arr)
    
# skyline([-1,1,1,7,-5,3])
skyline([0,4])
       