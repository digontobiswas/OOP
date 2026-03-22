
balace= 3000 #global variable

def buy_things(item, price):
    balace=500 #but i can declare a value for locally then global will be not accept at 1st i did bleow line . i just write comment for my future need. If read it carefully then i ca do it
    #if i use local variable then global will be not useable. 
    balace= balace-price  #overloading local variable i can't denote any same global variable locally
    print(f'balance after buying {item}', balace)

buy_things('sunglass', 1000) 
print('global balance after buy', balace)
#  Output is showing a error

# what is the soluation if i wannna use global and local and want to modify global variable bleow is the soluation
balace= 3000
def buy_things(item, price):
   
    global balace
    print('balance before buying sunglass',balace)
    balace= balace-price 
    print(f'balance after buying {item}', balace)

buy_things('sunglass', 1000) 
