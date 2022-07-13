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

# Zip it 

def zip_it(arr_1,arr_2):
    larger_arr = arr_1 if len(arr_1) > len(arr_2) else arr_2
    new_arr = []
    for i in range(len(larger_arr)):
        if i <= (len(arr_1)) -1:
            new_arr.append(arr_1[i])
        if i <= (len(arr_2))-1:
            new_arr.append(arr_2[i])  
    print(new_arr)
    

zip_it([4,15,100],[10,20,30,40])