from game_functions import seconds_to_hms


class GameState:
    def __init__(self):
        self.total_time=3600
        self.time_left=seconds_to_hms(self.total_time)
        self.current_down = 1
        self.current_team = 1
        self.specific_yard=0
        self.yards_to_gain = 10
        self.play_count=0

    def update_on_play(self, event_duration, yards_gained,current_team,file):
        if self.yards_to_gain == 10:
            file.write(f"There are {self.yards_to_gain} yards to gain! The current down is {self.current_down}!\n")
        file.write(f"Team {current_team.name} play took off {event_duration} seconds and gained {yards_gained} yards!\n")
        self.yards_to_gain -= yards_gained
        if self.yards_to_gain <= 0:
            file.write(f"Team {current_team.name} just got a first down!!!\n")
            self.reset_for_new_down()

        else:
            self.current_down += 1
            file.write(f"There are now {self.yards_to_gain} yards to gain! The current down is now {self.current_down}!\n")

        if self.current_down > 4:
            file.write(f"Team {current_team.name} turned the ball over!!!!\n")
            self.turnover()
        self.total_time-=event_duration
        self.time_left=seconds_to_hms(self.total_time)
        self.play_count+=1
        
    def reset_for_new_down(self):
        self.yards_to_gain = 10
        self.current_down = 1
        return "Reset for new down!"
    def turnover(self):
        self.specific_yard=0
        self.yards_to_gain = 10
        self.current_down = 1
        self.current_team = 1 if self.current_team == 2 else 2

    def field_traverse(self, yards_gained, team1, team2,file):
        self.specific_yard += yards_gained
        file.write(f"Time left: {self.time_left}\n")
        file.write(f"Yards left: {100 - self.specific_yard}\n")
        if self.specific_yard >= 100:
            if self.current_team == 1:
                team1.update_score()
                file.write(f"Team {team1.name} scored!!\n")
                file.write(f"Team {team1.name}'s score is now {team1.score}\n")

            else:
                team2.update_score()
                file.write(f"Team {team2.name} scored!!\n")
                file.write(f"Team {team2.name}'s score is now {team2.score}\n")


            self.specific_yard = 0
            self.current_team = 1 if self.current_team == 2 else 2

    def reset(self,team1,team2):
        self.total_time = 3600
        self.time_left = seconds_to_hms(self.total_time)
        self.current_down = 1
        self.current_team = 1
        self.specific_yard = 0
        self.yards_to_gain = 10
        self.play_count=0
        team1.score = 0
        team2.score=0

class Team:
    def __init__(self, offense, defense, score, name):
        self.offense = offense
        self.defense = defense
        self.score = score
        self.name=name
    def update_score(self):
        self.score += 7