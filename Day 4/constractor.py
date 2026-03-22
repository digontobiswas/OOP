class Phone:
    manufactured ='china'
    #onnanno programmming language e jete constractor python e seta __init__
    #constractor er kaj object gula k constract kora
    def __init__(self,owner,brand,price):
        self.owner=owner #self.owner hole attribute(attribute mane nam) = er pore owner mane perameter e asa owner er value
        self.brand=brand
        self.price=price  #coursore __init__ e rakhle dekha jabe Self@phone tahole phone er copy hobe ekhn e


    
    def send_sms(self, phone, sms):  #class er moddhe function k o method bole
        text=f'sending to:{phone} {sms}'
        print(text)

my_phone= Phone('kalachan','opoo' ,9800)      #kalachan owner,brand opoo price 9800
print(my_phone.owner,my_phone.brand,my_phone.price)
her_phone=Phone("Beauty","kindy",10000000)
print(her_phone.owner,her_phone.price,her_phone.brand)
    



