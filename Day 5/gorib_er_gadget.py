class Laptop:
    def __init__(self, brand,price,color,memory):
        self.brand= brand
        self.price=price
        self.color=color
        self.memory=memory
    
    def run(self):
        return f' running laptop: {self.brand}'
    def coding(self):
        return f'learing python and practicing'
    
class Phone:
    def __init__(self, brand, price, color, dual_sim):
        self.brand=brand
        self.price= price
        self.color= color
        self.dsim=dual_sim
    
    def run(self):
        return f'phone is running'

    def phone_call(self,number, text):
        return f'Sending SMS to: {number} with :{text}'
    
    """ There are many common things inside Phone class and laptop class
     like self.brand=brand
        self.price= price
        self.color= color
         those things are common attribute and run function is common method inside both class

         *****E i common and uncommon things gula ekta sundor vabe organise kora jay jate same kaj/code
         barbar na korte hoy. setar joinno ekta special relationship ace tar nam inheritence 
           """
