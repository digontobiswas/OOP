class Shop:
    cart=[]
    def __init__(self,byer):
        self.buyer_name=byer

    def add_to_cart(self,item):
        self.cart.append(item)

mefta =Shop('mefta')
mefta.add_to_cart('shoes')
mefta.add_to_cart('phone')
print(mefta.cart)

nisho=Shop('nisho')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart)   #nisho er card er moddhe mefta er cart er item chole asce ghotona ta ki object to alada
  #cart attribute ta sobar sathe  share able thake
  #constractor or instance er moddhe attribute use korle oita alada alada hobe

#uporer card chilo class attribute and nicher cart2 instance er moddhe so eta instance attribute so constractor oi person er joinno alada  array nibe alada alada hobe value eta hobe class attribute and instance attribute er difference
class Shopping:
    
    def __init__(self,byer):
        self.buyer_name=byer
        self.cart2=[]

    def add_to_cart(self,item):
        self.cart2.append(item)

meftaVai =Shopping('mefta')
meftaVai.add_to_cart('shoes')
meftaVai.add_to_cart('phone')
print(meftaVai.cart2)

nishoVai=Shopping('nisho')
nishoVai.add_to_cart('cap')
nishoVai.add_to_cart('watch')
print(nishoVai.cart2)


apurbo=Shopping('apurbo')
apurbo.add_to_cart('chiruni')
apurbo.add_to_cart('belt')
print(apurbo.cart2)