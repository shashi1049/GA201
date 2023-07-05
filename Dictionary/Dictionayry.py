'''Python dictionary is an ordered collection of items. 
- As of Python version 3.7, dictionaries are *ordered*. In Python 3.6 and earlier, dictionaries are *unordered*.
- Dictionaries are **optimized to retrieve values when the key is known.**
- A dictionary is a collection that is **changeable** and **does not allow duplicates**.
- Dictionaries are written **with curly brackets** and **have keys and values.**
- Holds data as `**key-value**` pair
- No concept of an index system and hence they are unordered.
- To fetch the data we use keys.
- A dictionary can’t have two keys with the same name. [ **keys must be unique and values can repeat**]
- Dictionaries are mutable, so we can
    - add a new key-value pair
    - replace the value not a key
    - delete a key-value pair'''

# syntax

'''dict={
	"key1": value,
	"key2": "value",
}'''

'''d = {
    'name': ["Anny", "Bunny", "Danny", "Enav"],
    'age': [25, 36, 22, 12],
    'income': [90, 75, 80, 93]
}
print(d['name'])  # ['Anny', 'Bunny', 'Danny', 'Enav']
print(len(d['name']))   # 4
print(d['name'][len(d['name'])-1])  # Enav
print(d['name'][len(d['name'])-1], " - ",
      d['age'][len(d['age'])-1])  # Enav  -  12

# For Loop
for i in range(len(d['name'])):
    print("Name -", d['name'][i], "Age -", d['age']
          [i], "Income(lakhs) -", d['income'][i])
'''
'''
OUTPUT => 
Name - Anny Age - 25 Income(lakhs) - 90
Name - Bunny Age - 36 Income(lakhs) - 75
Name - Danny Age - 22 Income(lakhs) - 80
Name - Enav Age - 12 Income(lakhs) - 93
'''

'''student = {
    "name": "Rahul",
    "age": 23,
    "nationality": "Indian",
    "location": "Nainital",
    "is_married": False,
    "highest_degree": "Btech"
}
print(student)
print(type(student))
'''

# Print the "brand" value of the dictionary:

'''thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])'''

# duplicate key will be replaced
'''thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020,
    "colors": ["red", "white", "blue"]
}
print(thisdict)
'''
# length of dictionary

'''Dict = {"name": "ABC", "age": 25, "City": "Delhi"}
print(len(Dict))      # 3
'''

'''
student = {
    "name": "Rahul",
    "age": 23,
    "nationality": "Indian",
    "location": "Nainital",
    "is_married": True,
    "highest_degree": "Btech"
}
if not student['is_married']:
    print("Naam to suna hi hoga")
else:
    print("Sunn ke koi fayda nahin")
'''
# get()
'''
Dict = {"name": "ABC", "age": 25, "city": "Delhi"}

print(Dict["name"])         # ABC
print(Dict.get("city"))     # Delhi
print(Dict["age"])          # 25
print(Dict.get("age"))      # 25
'''
# loop through dictionary

'''student = {
    "name": "Rahul",
    "age": 23,
    "nationality": "Indian",
    "location": "Nainital",
    "is_married": False,
    "highest_degree": "Btech",
    "pcm_marks": [12, 45, 78]
}

# Ist way to iterate in a python dictionary
for k in student:
    print(k, student[k])
    print("One key-value ends here")

# IInd way of iterating in a python dictionary
for k, v in student.items():
    print(k, ":", v)
'''

# updating value
'''Dict={"name": "ABC", "age": 25, "city": "Delhi"}

# Updating
Dict["age"]=26
print(Dict)        
# {'name': 'ABC', 'age': 26, 'city': 'Delhi'}
'''

# adding new key

'''Dict = {"name": "ABC", "age": 25, "city": "Delhi"}

# Adding
Dict["country"] = "India"
print(Dict)
# {'name':'ABC','age':26,'city':'Delhi','country':'India'}
'''

# pop()

'''Dict = {"name": "ABC", "age": 25, "city": "Delhi"}
Dict.pop("name")
print(Dict)
#  {'city': 'Delhi', 'country': 'India'}
'''

# popitem()

'''Dict = {"name": "ABC", "age": 25, "city": "Delhi", "country": "India"}
Dict.popitem()
print(Dict)          # {'name': 'ABC', 'age': 25, 'city': 'Delhi'}
'''

# clear all key-value pair
# clear()
'''
Dict = {"name": "ABC", "age": 25, "city": "Delhi", "country": "India"}
Dict.clear()
print(Dict)                   # {}
'''

# del keyword

'''Dict = {"name": "ABC", "age": 25, "city": "Delhi", "country": "India"}
del Dict["city"]
print(Dict)     # {'name': 'ABC', 'age': 25, 'country': 'India'}
del Dict
print(Dict)     # Throw Error as the Dict is deleted
'''

# keys()
'''
d = {
    'name': 'Sam',
    'department': 'Production',
    'age': 27
}
print(d.keys())  # dict_keys(['name', 'department', 'age'])
'''

# values()

'''d = {
    'name': 'Sam',
    'department': 'Production',
    'age': 27
}
print(d.values())  # dict_values(['Sam', 'Production', 27])
'''

# items()
# Return the list of tuples, where each tuple has a key-value pair of the dictionary.

d = {
    'name': 'Sam',
    'department': 'Production',
    'age': 27
}
print(d.items())
'''
OUTPUT =>
dict_items([('name', 'Sam'), ('department', 'Production'), ('age', 27)])
'''
