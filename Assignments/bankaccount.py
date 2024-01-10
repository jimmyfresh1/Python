class BankAccount:
    def __init__(self, rate, balance):
        self.rate = rate
        self.balance=balance
        self.update_container()
    def update_container(self):
            self.container = [self.rate, self.balance]

    def deposit(self,amount):
        self.balance += amount
        self.update_container()
        return self 
    
    def withdraw(self,amount):
        self.balance -=amount
        return self 
    
    def display(self):
        for info in self.container:
            print(info)
        return self 

    def yield1(self):
        self.balance+= self.balance * self.rate
        self.update_container()
        return self 

johns = BankAccount(.12 , 100)
jacks = BankAccount(.11, 200)
johns.deposit(70).deposit(80).deposit(10).withdraw(40).yield1().display()
jacks.deposit(20).deposit(30).withdraw(40).withdraw(10).withdraw(20).withdraw(30).yield1().display()
