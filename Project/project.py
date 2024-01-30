import os
from classes import GameState, Team
from game_functions import get_next_file_number, handle_play_simple, handle_play_post, handle_play_complex

logs_directory = 'logs'
os.makedirs(logs_directory, exist_ok=True)
algo_logs_directory = 'algo_logs'
os.makedirs(algo_logs_directory, exist_ok=True)


game_state = GameState()
team1= Team(9,3,0, "Fighting Ducks")
team2 = Team(2,7,0, "Dying Ducks")

def run_game (play_algo, log_file,algo_log_file):
    with open(log_file,'w') as file, open(algo_log_file, 'w') as algo_file:

        while game_state.total_time > 0:
            current_team = team1 if game_state.current_team == 1 else team2
            opposing_team = team2 if current_team == team1 else team1
            file.write(f"This is play {game_state.play_count}\n")
            algo_file.write(f"This is play {game_state.play_count}\n")
            event_duration, yards_gained= play_algo(current_team.offense,opposing_team.defense,algo_file)
            game_state.update_on_play(event_duration, yards_gained,current_team, file)
            game_state.field_traverse(yards_gained, team1, team2, file)


        file.write(f"Game Over! Final scores: Team 1 - {team1.score}, Team 2 - {team2.score}\n")
        if team1.score > team2.score:
            file.write("Team 1 wins!\n")
        elif team2.score > team1.score:
            file.write("Team 2 wins!\n")
        else:
            file.write("Tie!\n")
        if team1.score > team2.score:
            print ("Team 1 wins!")
        elif team2.score>team1.score:
            print ("Team 2 wins!")
        else:
            print ("Tie!")
    game_state.reset(team1,team2)

num_simulations = 1

for _ in range(num_simulations):
    num_a = get_next_file_number(os.path.join(logs_directory, 'game_log_a'), '.txt')
    num_b = get_next_file_number(os.path.join(logs_directory, 'game_log_b'), '.txt')
    num_c = get_next_file_number(os.path.join(logs_directory, 'game_log_c'), '.txt')

    run_game(handle_play_simple, os.path.join(logs_directory, f'game_log_a{num_a:02}.txt'), os.path.join(algo_logs_directory, f'algo_log_a{num_a:02}.txt'))
    run_game(handle_play_complex, os.path.join(logs_directory, f'game_log_b{num_b:02}.txt'), os.path.join(algo_logs_directory, f'algo_log_b{num_b:02}.txt'))
    run_game(handle_play_post, os.path.join(logs_directory, f'game_log_c{num_c:02}.txt'), os.path.join(algo_logs_directory, f'algo_log_c{num_c:02}.txt'))