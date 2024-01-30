import random
import os
import glob

logs_directory = 'logs'
os.makedirs(logs_directory, exist_ok=True)


class GameState:
    def __init__(self):
        self.current_down = 1
        self.yards_to_gain = 10
        self.current_team = 1

    def update_on_play(self, yards_gained):
        self.yards_to_gain -= yards_gained

        if self.yards_to_gain <= 0:
            self.reset_for_new_down()
        else:
            self.current_down += 1

            if self.current_down > 4:
                self.turnover()

    def reset_for_new_down(self):
        self.yards_to_gain = 10
        self.current_down = 1

    def turnover(self):
        self.current_down = 1
        self.yards_to_gain = 10
        self.current_team = 1 if self.current_team == 2 else 2

# Usage
game_state = GameState()
game_state.update_on_play(yards_gained=5)
# Update the game state based on the play outcome


def get_next_file_number(prefix, suffix):
    existing_files = glob.glob(f'{prefix}*{suffix}')
    max_num = 0
    for file in existing_files:
        num_part = file.replace(prefix, '').replace(suffix, '')
        if num_part.isdigit():
            max_num = max(max_num, int(num_part))
    return max_num + 1


def handle_downs_and_possession(current_down, yards_to_gain, yards_gained, current_team):
    yards_to_gain -= yards_gained
    if yards_to_gain <= 0:
        # First down achieved, reset downs and yards to gain
        yards_to_gain = 10
        current_down = 1
    else:
        current_down += 1
        if current_down > 4:
            # Turnover on downs, switch possession and reset downs and yards to gain
            current_down = 1
            yards_to_gain = 10
            current_team = 1 if current_team == 2 else 2

    return current_down, yards_to_gain, current_team


def simple_range_modifier(offense, defense):
    modifier = offense - defense
    low_end = max(0, modifier)
    high_end = 10 + modifier
    return random.randint(low_end, high_end)

def complex_range_modifier(offense, defense):
    offense_modifier = random.randint(offense - 2, offense + 2)
    defense_modifier = random.randint(defense - 2, defense + 2)
    modifier = offense_modifier - defense_modifier
    low_end = max(0, modifier)
    high_end = 10 + modifier
    return random.randint(low_end, high_end)

def post_calc_modifier(offense, defense):
    offense_modifier = random.randint(offense - 2, offense + 2)
    defense_modifier = random.randint(defense - 2, defense + 2)
    modifier = offense_modifier - defense_modifier
    return max(0, random.randint(0, 10) + modifier)

def handle_play_simple(offense, defense):
    event_duration = random.randint(20, 30)
    yards_gained = simple_range_modifier(offense, defense)
    return event_duration, yards_gained

def handle_play_complex(offense, defense):
    event_duration = random.randint(20, 30)
    yards_gained = complex_range_modifier(offense, defense)
    return event_duration, yards_gained

def handle_play_post(offense, defense):
    event_duration = random.randint(20, 30)
    yards_gained = post_calc_modifier(offense, defense)
    return event_duration, yards_gained


def update_score_and_possession(current_team, yards_gained, score):
    yards =0
    yards += yards_gained
    if yards >= 100:
        score += 1
        yards = 0
        current_team = 1 if current_team == 2 else 2
    return current_team, yards, score

def seconds_to_hms(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return "{:02d}:{:02d}:{:02d}".format(h, m, s)

def run_game (play_algo, log_file):
    with open(log_file,'w') as file:
        total_time = 3600  
        yards = 0
        team1_score, team2_score = 0, 0
        current_team = 1
        team1_offense, team1_defense = 8, 3
        team2_offense, team2_defense = 3, 8

        while total_time > 0:
            if current_team == 1:
                offense = team1_offense
                defense = team2_defense
            else:
                offense = team2_offense
                defense = team1_defense
            
            event_duration, yards_gained= play_algo(offense,defense)    
            total_time -= event_duration
            time_left = seconds_to_hms(total_time)

            if current_team == 1:
                yards += yards_gained
                file.write(f"Team {current_team} play took off {event_duration} seconds and gained {yards_gained} yards!\n")
                file.write(f"Time left: {time_left}\n")
                file.write(f"Yards left: {100 - yards}")
                print("Team 1 play took off " + str(event_duration) + " seconds and gained " + str(yards_gained) + " yards!")
                print("Yards left:", (100-yards))
                if yards >= 100:
                    team1_score += 1
                    yards = 0
                    print("Team 1 scores! Total scores:", team1_score)
                    current_team = 2  # Switch possession to team 2
            else:
                yards += yards_gained
                file.write(f"Team {current_team} play took off {event_duration} seconds and gained {yards_gained} yards!\n")
                file.write(f"Time left: {time_left}\n")
                file.write(f"Yards left: {100 - yards}")
                print("Team 2 play took off " + str(event_duration) + " seconds and gained " + str(yards_gained) + " yards!")
                print("Yards left:", (100-yards))
                if yards >= 100:
                    team2_score += 1
                    yards = 0
                    print("Team 2 scores! Total scores:", team2_score)
                    current_team = 1  # Switch possession to team 1

            print("Time left:", time_left)
        file.write(f"Game Over! Final scores: Team 1 - {team1_score}, Team 2 - {team2_score}\n")
        if team1_score > team2_score:
            file.write("Team 1 wins!\n")
        elif team2_score > team1_score:
            file.write("Team 2 wins!\n")
        else:
            file.write("Tie!\n")
        print("Game Over! Final scores: Team 1 -", team1_score, ", Team 2 -", team2_score)
        if team1_score > team2_score:
            print ("Team 1 wins!")
        if team2_score>team1_score:
            print ("Team 2 wins!")
        else:
            print ("Tie!")

num_simulations = 5

for _ in range(num_simulations):
    num_a = get_next_file_number(os.path.join(logs_directory, 'game_log_a'), '.txt')
    num_b = get_next_file_number(os.path.join(logs_directory, 'game_log_b'), '.txt')
    num_c = get_next_file_number(os.path.join(logs_directory, 'game_log_c'), '.txt')

    run_game(handle_play_simple, os.path.join(logs_directory, f'game_log_a{num_a:02}.txt'))
    run_game(handle_play_complex, os.path.join(logs_directory, f'game_log_b{num_b:02}.txt'))
    run_game(handle_play_post, os.path.join(logs_directory, f'game_log_c{num_c:02}.txt'))