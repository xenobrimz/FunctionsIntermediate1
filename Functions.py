#Update Values in Dictionaries and Lists
#1.
x = [ [5,2,3], [10,8,9] ] 

x[1][0] = 15
print(x)

#2.
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[1]['last_name'] = 'bryant'
print(students[1]['last_name'])

#3.
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'][0])

#4.
z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)

#Iterate Through a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for i in range(len(students)):
        print('first_name' +' - '+ students[i]['first_name']+' - '+ 'last_name' +' - '+  students[i]['last_name'])

iterateDictionary(students)

# Get Values From a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        if key_name == 'first_name':
            print(some_list[i]['first_name'])
        elif key_name == 'last_name':
            print(some_list[i]['last_name'])
        else:
            print("keyname not found")

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)
iterateDictionary2('middle_name', students)

# Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    items = 0
    for i,j in some_dict.items():
        items = len(j)
        print(str(items) + ' ' + i)
        for k in j:
            print(k)
        print(' ')
        
       
                  
printInfo(dojo)

room_num = {'john': 425, 'tom': 212, 'isaac': 345}
for k, v in reversed(room_num.items()):
    print (k + ' is in room ' + str(v))