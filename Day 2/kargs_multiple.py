def full_name(first, last):
    name=f'full name is: {first} {last}'
    return name
#take parameter as in order(serial wise)
# name=full_name('alu', "kodu")


#take parameter as not in order(not serial wise)
name=full_name(last='kodu', first='alu')

print(name)

# if you input as not in order function will be output always as in order
def famous_name(frist, last, aditional):
     name=f'{frist} {last} {aditional}'
     return name

nam=famous_name(frist='taheri', aditional='ali', last='khan')
print(nam)

# if you ar not input all perameter then nothing will hapen if we use args but if we don't use args then output will be error
def famous_name(frist, last, *aditional):
     name=f'{frist} {last} '
     return name

nam=famous_name(frist='taheri', last='khan')
print(nam)

#we can use double * before a function parameter and it can print multiple kargs(key parameter)
def famous_name(frist, last, **aditional):
     name=f'{frist} {last} '
     #print(aditional) #it will be print like a set args with key or title that's why it's call kargs
     #print(aditional['title']) #we can print individul key by this formate.hujur is title this will be output

    # we can use for loop for print key will values or item
     for key, value in aditional.items():
        print(key, value)
     return name

nam=famous_name(frist='taheri', last='khan', title='hujur', extra= 'shayok' )
print(nam)

# we can return multiple things from  a function

def a_lot (num1, num2):
    sum= num1+num2
    mult=num1*num2
    sub=num1-num2
    return sum, mult, sub

everything= a_lot(55,21)
print(everything)  #it will be print like tuple
