age =45
interest_rate=2.5
name='somaip'
distric='patuakhali'
is_single = True
is_sleeping =True

print(age)
print(name)
print(age+interest_rate)
print(type(age)) #by using it we can know variable type



# single line comment Ctrl+/

#Multiple line comment Alt+Shift+A
""" print(age)
print(name)
print(age+interest_rate)
print(type(age))
print() """

# print()
# adding two or more string
print('kodom ali'+ 'kacha badam') #here ali and kacha added in single word
print('kodom ali'+' '+ 'kacha badam') #here by using this tecnique ali and kacha added in indivisual word


# F string
text = f"kodom ali {age} living in {distric}. intersting with rate {interest_rate}"
print(text)