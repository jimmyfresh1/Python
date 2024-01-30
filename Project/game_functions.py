import random
import glob
import os

def seconds_to_hms(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return "{:02d}:{:02d}:{:02d}".format(h, m, s)


def simple_range_modifier(offense, defense,algo_file):
    algo_file.write(f"Offense is was {offense}\n")
    algo_file.write(f"Defense is was {defense}\n")
    modifier = offense - defense
    algo_file.write(f"Modifier was {modifier}\n")

    low_end = max(0, modifier)
    algo_file.write(f"Low end was {low_end}\n")
    high_end = 10 + modifier
    algo_file.write(f"High end was {high_end}\n")
    return random.randint(low_end, high_end)

def complex_range_modifier(offense, defense,algo_file):
    offense_modifier = random.randint(offense - 2, offense + 2)
    algo_file.write(f"Complex Range Offense modifier was {offense_modifier}\n")
    defense_modifier = random.randint(defense - 2, defense + 2)
    algo_file.write(f"Complex Range Defense modifier was {defense_modifier}\n")
    modifier = offense_modifier - defense_modifier
    algo_file.write(f"Complex Range Final modifier was {modifier}\n")
    low_end = max(0, modifier)
    high_end = 10 + modifier
    return random.randint(low_end, high_end)

def post_calc_modifier(offense, defense,algo_file):
    offense_modifier = random.randint(offense - 2, offense + 2)
    algo_file.write(f"Post Calc Offense modifier was {offense_modifier}\n")
    defense_modifier = random.randint(defense - 2, defense + 2)
    algo_file.write(f"Post Calc defense modifier was {defense_modifier}\n")
    modifier = offense_modifier - defense_modifier
    algo_file.write(f"Post Calc Final modifier was {modifier}\n")
    return max(0, random.randint(0, 10) + modifier)

def handle_play_simple(offense, defense,algo_file):
    event_duration = random.randint(30, 40)
    yards_gained = simple_range_modifier(offense, defense,algo_file)
    algo_file.write(f"This play gained {yards_gained} yards\n")
    return event_duration, yards_gained

def handle_play_complex(offense, defense, algo_file):
    event_duration = random.randint(30, 40)
    yards_gained = complex_range_modifier(offense, defense,algo_file)
    algo_file.write(f"This play gained {yards_gained} yards\n")
    return event_duration, yards_gained

def handle_play_post(offense, defense,algo_file):
    event_duration = random.randint(30, 40)
    yards_gained = post_calc_modifier(offense, defense,algo_file)
    algo_file.write(f"This play gained {yards_gained} yards\n")
    return event_duration, yards_gained

def get_next_file_number(prefix, suffix):
    existing_files = glob.glob(f'{prefix}*{suffix}')
    max_num = 0
    for file in existing_files:
        num_part = file.replace(prefix, '').replace(suffix, '')
        if num_part.isdigit():
            max_num = max(max_num, int(num_part))
    return max_num + 1


# def update_score_and_possession(current_team, yards_gained, score):
#     yards =0
#     yards += yards_gained
#     if yards >= 100:
#         score += 1
#         yards = 0
#         current_team = 1 if current_team == 2 else 2
#     return current_team, yards, score



# def handle_downs_and_possession(current_down, yards_to_gain, yards_gained, current_team):
#     yards_to_gain -= yards_gained
#     if yards_to_gain <= 0:
#         # First down achieved, reset downs and yards to gain
#         yards_to_gain = 10
#         current_down = 1
#     else:
#         current_down += 1
#         if current_down > 4:
#             # Turnover on downs, switch possession and reset downs and yards to gain
#             current_down = 1
#             yards_to_gain = 10
#             current_team = 1 if current_team == 2 else 2

#     return current_down, yards_to_gain, current_team