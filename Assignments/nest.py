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

x[1][0]=15
print(x)
students[0]["last_name"]= "Bryant"
print(students)

sports_directory['soccer'][0]='Andres'
print(sports_directory)

z[0]['y']=30
print(z)

##2
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(my_list): 
    for student in my_list:
            print(student)
iterateDictionary(students)

##3
def iterateDictionary2(key_name, my_list):
    for student in my_list:
            print (student[key_name])
iterateDictionary2('first_name', students)

#4


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}



def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[f'{key}']), key,some_dict[f'{key}'])

printInfo(dojo) 