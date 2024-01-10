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
    
class User:
    def __init__(self,name,email, which_act):
        self.name=name
        self.email=email
        self.act_dict = {}
        self.add_account(which_act)

    def add_account (self, which_act):
        self.act_dict[which_act] = BankAccount(rate=.02,balance=10)
    def bank_deposit(self, which_act, amount):
        self.act_dict[which_act].deposit(amount)
        print(self.act_dict[which_act].balance)
    def bank_withdraw(self,which_act,amount):
        self.act_dict[which_act].withdraw(amount)
        print(self.act_dict[which_act].balance)
    def bank_balance(self, which_act):
        self.act_dict[which_act].display()
    def transfer_money(self, amount, other_user, which_act, their_act):
        self.act_dict[which_act].withdraw(amount)
        other_user.act_dict[their_act].deposit(amount)
        print(self.name + "gave" + str(self.act_dict[which_act].balance))
        print(other_user.name + "gained" + str(other_user.act_dict[their_act].balance))
        return self



# johns = BankAccount(.12 , 100)
# jacks = BankAccount(.11, 200)
# johns.deposit(70).deposit(80).deposit(10).withdraw(40).yield1().display()
# jacks.deposit(20).deposit(30).withdraw(40).withdraw(10).withdraw(20).withdraw(30).yield1().display()

jakes= User( "Jake from State Farm", "maauto@gmail.com", 'savings')
jakes.bank_deposit('savings', 60)
jakes.add_account('pokemon')
jakes.bank_deposit('pokemon', 10)
jakes.bank_deposit('savings', 60)
bob= User ("Bobby Lazearound", "icup@gmail.com", "checking")
bob.bank_deposit("checking", 20)
print(jakes.act_dict)
jakes.transfer_money(40, bob, 'pokemon', 'checking' )
bob.bank_balance('checking')