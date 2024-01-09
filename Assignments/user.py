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
    def enroll(self):
        if self.rewards_bro == False:
            self.rewards_bro= True
            self.points+=200
        else: 
            print('yo stop')
            return 
    def spend_points(self, amount):
        if self.points < amount:
            print('no')
            return
        self.points -= amount 


John = User("John", "Connor", "StopDaMachines@Cyberdyne.skynet", 'The Perfect Age to Terminate')
John.display()
John.enroll()
print (John.rewards_bro)
John.spend_points(50)
print(John.points)
John.enroll()

Jack = User ("Jack", "Sparrow", "TheBestPirateYouveEverMet@DutchIndiaCompany.sea", 30)
Jack.display()
Jack.spend_points(80)

Ben= User ("Benjamin", "Button", "blah@blah.blah", "A lot older than you think" )
Ben.display()
Jack.spend_points(210)