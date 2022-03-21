# 1 update values in dictionary

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15. 

x[1][0] = 15
print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
# this makes no sense

students[0]['last_name'] = "Bryant"
print(students)

# In the sports_directory, change 'Messi' to 'Andres'

sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

# Change the value 20 in z to 30

z[0]['y'] = 30
print(z)


# 2 


students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)

def iterate_dictionary(list):
    for i in range(0,len(list)):
        output = ""
        for key,val in list[i].items():
            output += f"{key} - {val},"
        print(output)

iterate_dictionary(students)


# 3

def iterate_dictionary(key_name,list):
    for i in range(0,len(list)):
        for key,val in list[i].items():
            if key == key_name:
                print(val)

iterate_dictionary('first_name',students)
iterate_dictionary('last_name',students)

# 4

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# My work
def printInfo(list):
    print(len(list['locations']),"Locations")
    for i in range(0,len(list['locations'])):
        print(list[i])


printInfo(dojo)

# Solution 
def print_info(dict):
    for key,val in dict.items():
        print("--------------")
        print(f"{len(val)} {key.upper()}")
        for i in range(0, len(val)):
            print(val[i])

print_info(dojo)