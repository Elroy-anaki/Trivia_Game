from functions import *


def main():    
 
    PLAYERS = Player().create_players(args.num_of_players)
    QUESTIONS = load_from_json_file_to_list(args.file_path)
    DIFFICULTY_LEVELS = ["Easy", "Medium", "Hard"]
    ANSWERS_OPTIONS = ["1", "2", "3", "4"]
    
    selected_question = select_filters(QUESTIONS, DIFFICULTY_LEVELS)
    player_index = 0
    
    while True:
        time.sleep(1)
        print(f"\n{PLAYERS[player_index].name}, , your turn\nThe question:\n{selected_question}")
        answer = valid_input(input("Enter your answer: "), ANSWERS_OPTIONS).strip().title()
        
        if PLAYERS[player_index].is_correct(answer, selected_question._correct_answer):
            time.sleep(1)
            print("Correct answer, Well Done!!!")
            PLAYERS[player_index].add_point()
            QUESTIONS.remove(selected_question)
            if not QUESTIONS:
                break
            selected_question = select_filters(QUESTIONS, DIFFICULTY_LEVELS)
            player_index += 1
            
        else:
            time.sleep(1)
            print("Wrong answer!")
            player_index += 1
            
            
        if player_index == len(PLAYERS):
            player_index = 0

          
    display_winners(PLAYERS)

          
if __name__ == "__main__":
    args = parser_Argument()
    main()
