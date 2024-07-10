from functions import *


def main():    
 
    PLAYERS = Player().create_players(args.num_of_players)
    QUESTIONS = get_from_json_file(args.file_path)
    DIFFICULTY_LEVELS = ["Easy", "Medium", "Hard"]
    selected_question = user_choice(QUESTIONS, DIFFICULTY_LEVELS)
    player_index = 0
    
    while True:
        time.sleep(1)
        print(f"{PLAYERS[player_index].name}, , your turn\nThe question:\n{selected_question}")
        answer = proper_answer(input("Enter your answer: "))
        
        if PLAYERS[player_index].check_answer(answer, selected_question._correct_answer):
            time.sleep(1)
            print("Correct answer, Well Done!!!")
            QUESTIONS.remove(selected_question)
            if not QUESTIONS:
                break
            selected_question = user_choice(QUESTIONS, DIFFICULTY_LEVELS)
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
