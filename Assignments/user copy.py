class User:
    rewards_bro = False
    points = 0
    def __init__(self,first_name,last_name,email, age):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        self.container= [self.first_name, self.last_name, self.email, self.age]

    def display(self):
        for info in self.container:
            print(info)
        return self
    def enroll(self):
        if self.rewards_bro == False:
            self.rewards_bro= True
            self.points+=200
            return self
        else: 
            print('yo stop')
            return self
    def spend_points(self, amount):
        if self.points < amount:
            print('no')
            return self
        self.points -= amount 
        return self


John = User("John", "Connor", "StopDaMachines@Cyberdyne.skynet", 'The Perfect Age to Terminate')
John.display().enroll().spend_points(50).display()
print (John.rewards_bro)
John.spend_points(50)
print(John.points)

Jack = User ("Jack", "Sparrow", "TheBestPirateYouveEverMet@DutchIndiaCompany.sea", 30)
Jack.display().spend_points(80)
print(Jack.points)

Ben= User ("Benjamin", "Button", "blah@blah.blah", "A lot older than you think" )
Ben.display()
Ben.spend_points(210)