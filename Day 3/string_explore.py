name ='sakib khan'
name2 = "kader ali"
# this is a multiline string
name3="""
sakib khan number one
"""

print(name)
print(name2)
print(name3)


#if i wanna write sakib's khan
#this is called escape i need to explore more escape
name4='sakib\'s khan'
print(name4)
name5= "masud's khan"
print(name5)

# Mutable means changeable
# string is a sequence og characters. but immmutable. It's similar to list but list is mutable

# prove string a sequence of characrter
for char in name3:
    print(char)  #print will be every charracter

print(name2[2]) #index 2 in name2 will be print
print(name[::-1])  #print will be reverse

""" 
prove string is not mutable
name2[0]='R'
print(name2) 
This will be give a error and said str object does not support  item assignment
so provbe that string in not mutable(changable)
 """
# find
if 'khan' in name2:
    print("ACHE")
else:
    print('NAI')


if 'khan' in name:
    print("ACHE")
else:
    print('NAI')

# UPPER
print(name2.upper())

# SAME WAY WE CAN SEE STRING METHOD FROM GEEKSFORGEEKAS AND FROM PROGRAMMING METHOD


