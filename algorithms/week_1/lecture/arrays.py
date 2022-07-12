import random
# shuffling the numbers inside an array
def shuffle(arr):
    new_arr = []
    for i in range(len(arr)):
        random_index = random.randint(0,len(arr)-1)
        new_arr.append(arr[random_index])
        arr.pop(random_index)
    return new_arr

print(shuffle([43,21,78,9,7,2])) # shuffle this 