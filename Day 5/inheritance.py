# common class
class Device:
    def __init__(self, brand, price, color):
         #common attribute only
         self.brand= brand
         self.price=price
         self.color=color

    #common functionality
    def run(self):
        return f' running laptop: {self.brand}'
        
class Laptop:
    def __init__(self,memory):
       
        self.memory=memory
    
   
    def coding(self):
        return f'learing python and practicing'
    
class Phone(Device):
    def __init__(self, dual_sim,brand,price, color):
        self.dsim=dual_sim
        super().__init__(brand, price, color)
    def phone_call(self,number, text):
        return f'Sending SMS to: {number} with :{text}'
    def __repr__(self):
        return f'Phone: {self.dsim}, Brand name:{self.brand},color is:{self.color},price is:{self.price}'
                
                
                
    
class Camera:
    def __init__(self, pixel):
        self.pixel= pixel

    def change_lens(self):
        pass
#  inheritance
my_phone=Phone(True,'samsung', 2000, 'black')
my_phone.phone_call(112233,'Hello pio')
print(my_phone)