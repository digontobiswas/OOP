def all_sum(*numbers): # for sending more than one parameter i just use tuple by giving a * before parameter
    print(numbers)
total_number=all_sum(10,20,30) #output will be a list of tuple of all parameter

#as a tuple or looks like list of set we can see it indivisually by using fo loop

def sum(*values):
    for i in values:
        print(i)
      
sum(100,200,300,400)

# if we use special parameter for frist 2 , then we can make tuple also see in the bleow section

def hello(num1,num2, *var):
    for x in var:
        print(x)  # 10 ,20 will be not output as tuple becuase they are specially in parameter
total=hello(10,20,30,40,50)
print(total)

#generally people * er pore args use kore onno kisu na lihke ex: def hello(num1,num2, *args), ami amar moto likte parbo problem nai


