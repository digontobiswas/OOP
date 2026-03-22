# list []
# tuple ()
# set {}

# set: unique items collection

numbers=[12,56,98,78,56,12,6,98]
number_set=set(numbers) # print will be just unique and inside {} brackets
print(number_set)

# add remove/drive, check, a loop possible but don't can access by index. so add/remove in particular possition not possible

# add in set

number_set.add(55)
print(number_set) 

# remove 
number_set.remove(55)
print(number_set)

# drive a loop
for item in number_set:
    print(item)

#check
if 56 in number_set:
    print('have 56')

else:
    print("have not 56")
# union

A={1,2,3}
B={4,5,6}
print(A & B)
print(set(A).union(B))