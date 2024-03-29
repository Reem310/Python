#Update Values in Dictionaries and Lists
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

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0]=15

# Change the last_name of the first student from 'Jordan' to 'Bryant'
# students[1].'lastname'='Bryant'
students[0]['last_name']='Bryant'

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0]='Andres'

# Change the value 20 in z to 30
z[0]['y']=30

#Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(my_list):
    for i in range (len(my_list)):
        print("first_name - "+my_list[i]['first_name']+", last_name - " +my_list[i]['last_name'])
    
    for student in my_list:
        print("first_name - "+student['first_name']+", last_name - " +student['last_name'])




# Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and 
# a key name, the function prints the value stored in that key for each dictionary. 
def iterateDictionary2(key_name, some_list):
    for student in some_list:
        print(student[key_name])



# Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name 
# of each key along with the size of its list, and then prints the associated values within each key's list. 
dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for x in some_dict:
        print(len(some_dict[x]),x.upper())
        for i in some_dict[x]:
            print(i)
printInfo(dojo)