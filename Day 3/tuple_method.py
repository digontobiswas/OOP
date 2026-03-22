def multiple():
    return 3,4 # for this comma it's converted as tuple
print(multiple()) #output will be a tuple

things ='pen', #for this comma it's converted as a tuple
print(things)

items='plte', 'muri','khoi', 'charger', 'botale' ,'laptop', 'webcam' ,'chatu' ,'chira' #for this comma it's converted as tuple
print(items)

# we can see any index number in tuple
print(items[0])

print(items[ 3:6])  # we can do same as list
print(items[-2])

if 'webcam' in items:
    print('ache')

# we cna't change tuple itself but we can change list that contain a tuple
mega=(1,2,3) # It's a tuple
print(mega) 
print(mega[1])
# mega[1]=3 not posible change like that if i commetout this then i can see the error
print(mega)

# we can change like this
mega2=([1,2,3],[50,55,65],[100,200,300]) #this is tuple and every index contain a list we can change inside the list
mega2[1][1]=4000 #tuple er index 1 er list er moddher lister 1 index value change hobe
print(mega2)


