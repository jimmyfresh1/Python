players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32,
        "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]


class Player ():
    def __init__(self, some_dict): 
        self.name =some_dict["name"]
        self.age = some_dict["age"]
        self.position =some_dict["position"]
        self.team = some_dict["team"]
        self.container=some_dict
    def display(self):
        print(self.container)
    
    @classmethod
    def get_team(cls, some_list):
        instance_list=[]
        for player in some_list:
            instance_list.append(cls(player))
            
        for player_stats in instance_list:
            player_stats.display()
        return instance_list


# Challenge 1 and 2 finished but commented out 
# kevin = Player((players[0]))
# jason= Player((players[1]))
# kyrie = Player((players[2]))

# new_team= []
# for player in players:
#     new_team.append(Player(player))
# new_team[0].display()

team_list= Player.get_team(players)