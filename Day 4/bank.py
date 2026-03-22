class Bank:
    def __init__(self,balance):
        self.balance=balance
        self.min_withdrow=100
        self.mx_withdrow=100000
    
    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount>0:
            self.balance+=amount
    
    def withdraw(self,amount):
        if amount <self.min_withdrow:
            print(f'you can not withdraw blew{self.min_withdrow}') 

        elif amount >self.mx_withdrow:
            print(f'bank fokir hoye jabe') 
        
        else:
            self.balance -= amount
            print(f'here is your money {amount}') 
            print(f'your money after withdraw {self.balance}')
            # same things will be happen. we can call a method into another method
            print(f'your money after withdraw {self.get_balance()}')

brac =Bank(15000)
brac.withdraw(25)
brac.withdraw(500000)
brac.withdraw(500)

dbbl = Bank(5000)
dbbl.deposit(2000)
print(dbbl.get_balance())
