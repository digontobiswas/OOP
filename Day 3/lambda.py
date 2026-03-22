#lambda

def double(x):
    return x*2

result=double(44)
print(result)

# we can use this double function by using lambda
doubled =lambda num : num *2 # 1st num write for perameter then after this(:) just write functional work
print(doubled(50))

# we can do any mini function by using lambda

# multiple parameter lambda function
add =lambda x,y: x+y
sum=add(11,33)
print(sum)

numbers=[12,56,98,78,56,12,6,98]
dub_num= map(doubled,numbers) #lambda functiobn er under a kono function er nam and kon variable k korbo oi variable er nam
#map(lambda_funtion_under_function_name, kon_variable_k_korbo_oi_varibale_nam)
print(numbers)
print(list(dub_num))

#we can use lambda funtion directly inside map

marks=[198,56,77,44,77,99,22]
dub_marks=map(lambda m: m*2,marks)
print(marks)
print(list(dub_marks))

actors=[
    {'name':'sabana', 'age':65},
    {'name':'alomgir', 'age':45},
    {'name':'sabila nor', 'age':30},
    {'name':'amitab', 'age':38},
    {'name':'sakib khan', 'age':47}
    ] # actor  list and inside list have dictionary

#  have filter build in  that can use under lambda function

#junior filter kortechi
juniors=filter(lambda actor:actor['age']<40, actors)
print(list(juniors))

