numbers=[12,56,98,78,56,12,6,98]
# A person detils
person1=['kala chan', 'kalipur', 23,' student']
# key value pair
# dictionary
# object
# hash table
# overlap with set

person= {'name':'kala pakhi', 'address':'Kalipkpur','age':22, 'job':'student'}
#here name is key and kala pakhi is value same for all like address is key and job is key and address is key rest are the valu of those key
#this is a dictionary and dictionary is key value pair
print(person)
print(person['job']) # here  job is key, inside the person dictionary value will ve print under job key

# print will be all keys
print(person.keys())

# print will be all values
print(person.values())

# add key and value inside the dictionary
person['language']='python'
print(person['language'])
print(person.keys())
# del any key
del person['age']
print(person)

# special dictionary looping
for key, value in person.items():
    print(key ,":" ,value  )





