numbers= [45,87,65,43,85,14,26,61]
odds=[]
for num in numbers:
    if num %2 ==1:
        odds.append(num)

print(odds[:])  #print will be just odds number

numbers= [45,87,65,43,85,14,26,61]
odds_and_Div_BY5=[]
for num in numbers:
    if num %2 ==1 and num%5==0:
        odds_and_Div_BY5.append(num)

print(odds_and_Div_BY5[:])  #print will be just odds number that divided by 5

#we can do same things in onelie

odd_numbers=[num for num in numbers if num%2==1] #num 1st time for declare variable and then write loop and condition but this is not readable, so i'll be ignor to do it
print(odd_numbers)

#nasted for loop 
players=['sakib', 'musfik','liton']
ages=[38,37,32]
age_com=[]
for player in players:
    print('player:',player)
    for age in ages:
        print(player,age)
        age_com.append([player,age])
print(age_com)  #print all age combination


#nasted for loop same in sortcut but not meaning full not readable so i'll try to ignor it
age_comb2=[player for player in players for age in ages]
print(age_comb2)





