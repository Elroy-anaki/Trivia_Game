from functions import *
from Player import Player

DIFFICULTY_LEVELS = ["Easy", "Medium", "Hard"]
ANSWERS_OPTIONS = ["1", "2", "3", "4"]

def main():    
 
    players = Player().create_players(args.num_of_players)
    questions = load_from_json_file_to_list(args.file_path)
    
    
    selected_question = select_filters(questions, DIFFICULTY_LEVELS)
    player_index = 0
    
    while True:
        time.sleep(1)
        print(f"\n{players[player_index].name}, , your turn\nThe question:\n{selected_question}")
        answer = valid_input(input("Enter your answer: "), ANSWERS_OPTIONS).strip().title()
        
        if players[player_index].is_correct(answer, selected_question._correct_answer):
            time.sleep(1)
            print("Correct answer, Well Done!!!")
            players[player_index].add_point()
            questions.remove(selected_question)
            if len(questions) == 0:
                break
            selected_question = select_filters(questions, DIFFICULTY_LEVELS)
            player_index += 1
            
        else:
            time.sleep(1)
            print("Wrong answer!")
            player_index += 1
            
            
        if player_index == len(players):
            player_index = 0

          
    print_winners(players)

          
if __name__ == "__main__":
    args = parse_arguments()
    main()
