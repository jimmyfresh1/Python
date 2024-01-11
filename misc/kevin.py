kevin = {"name": "Kevin Durant" , "age":34, "position": "small forward", "team":"Brooklyn Nets"}

class Player:
    def __init__(self, name,age,position, team): 
        self.name =name
        self.age = age
        self.position =position
        self.team = team
        self.update_container()

    def update_container(self):
        self.container = [self.name,self.age,self.position,self.team]   
    def display(self):
        print(self.container)


player_kevin = Player(kevin["name"], kevin["age"], kevin["position"], kevin["team"])
player_kevin.display()
