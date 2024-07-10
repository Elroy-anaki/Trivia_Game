import argparse
import random
import json
import time
from classes import *

def parser_Argument() -> argparse.Namespace:
    """
    Parses command-line arguments for the Trivia Game.

    The function uses the argparse module to define and parse command-line arguments
    for the Trivia Game. It requires two arguments:
    --file_path: A string representing the path to the JSON file with questions.
    --num_of_players: An integer representing the number of players in the game.

    Returns:
        argparse.Namespace: An object containing the values of the parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Trivia Game.")
    parser.add_argument('--file_path', type=str, required=True, help='Path to the JSON file with questions')
    parser.add_argument('--num_of_players', type=int, required=True, help='Number of players in the game')
    result = parser.parse_args()
    return result


def get_from_json_file(file_path: str) -> list:
    """
     Loads questions from a JSON file and adds them to the question bank.
        
    Args:
        file_path (str): The path to the JSON file containing the questions.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
    lst = []
    for i in data["questions"]:
        q = Question(
            question=i["question"],
            answers=i["answers"],
            correct_answer=i["correct_answer"],
            category=i["category"],
            difficulty=i["difficulty"]
            
            )
        lst.append(q)
    return lst


def get_random_questions(lst) -> Question:
    """
    Returns a list of randomly selected questions from the question bank.
    
    Args:
        list_of_questions (int): The list of questions the function choose from.
        
    Returns:
        Question: A Question object.
    """
    
    return random.choice(lst)


def is_valid_input(answer_of_user: str) -> tuple[bool, str]:
    """Checks if user's input is valid (only 1 digit between 1 - 4)

    Args:
        answer_of_user (str): The user's answre

    Returns:
        tuple[bool, str]: Tuple of bool object and message
    """
    if len(answer_of_user) > 1:
        return False, "Only 1 digit",
    elif answer_of_user > "4" or answer_of_user == "0":
        return False, "Only between 1 - 4"
    return True, ""
    
    
def proper_answer(answer_of_user: str) -> str:
    """Forces the user to choose proper answer (only 1 digit between 1 - 4)

    Args:
        answer_of_user (str): The user's answre

    Returns:
        str: The proper user's answre
    """
    valid, message = is_valid_input(answer_of_user)
    while not valid:
        print(f"{message}, Try again")
        answer_of_user = input("Enter your answer: ")
        valid, message = is_valid_input(answer_of_user)
    return answer_of_user


def get_categories(questions_list: list[object]) -> set[str]:
    """Gets the Available categories from the questions' list

    Args:
        questions_list (list[object]): The questions' list

    Returns:
        set[str]: The Available categories
    """
    categories = []
    for q in questions_list:
        categories.append(q.category)
    return set(categories)
    

def proper_user_choose(user_choose: str, options: list[str]) -> str:
    """Checks if the user choose exist in the options

    Args:
        user_choose (str): string (category or difficulty level)
        options (list[str]): list of options to choose from

    Returns:
        str: The proper user's choose 
    """
    while user_choose not in options:
        user_choose = input(f"Invalid choose, choose only from these options {options}: ")
        
    return user_choose


def user_choice(QUESTIONS: list[object], DIFFICULTY_LEVELS: list[str]) -> object:
    """Returns a random question during the game by user's choice

    Args:
        QUESTIONS (list[object]): Questions' list
        DIFFICULTY_LEVELS (list[str]): Difficulty levels' list

    Returns:
        object: A random question
    """
    categories = get_categories(QUESTIONS)
    print(f"Available categories: {categories}")
    user_category = proper_user_choose(input("Choose category: "), categories)
    user_difficulty = proper_user_choose(input("Choose difficulty level: "), DIFFICULTY_LEVELS)
    corrent_list = filter_list(user_category, user_difficulty, QUESTIONS)
    selected_question = get_random_questions(corrent_list)
    return selected_question


def filter_list(category: str, difficulty: str, questions: list[object]) -> list[object]:
    """Filters the whole questions' list to the filtered list by user choice

    Args:
        category (str): User_input
        difficulty (str): User_input
        questions (list[object]): Questions list

    Returns:
        list[object]: The filtered list of questions
    """
    filtered_list = [q for q in questions if q.category == category and q.difficulty == difficulty]
    while not filtered_list:
        print("There is no questions in these filters.")
        category = input("Choose category again: ")
        difficulty = input("Choose difficulty level again: ")
        filtered_list = [q for q in questions if q.category == category and q.difficulty == difficulty]
    return filtered_list


def fix_player_index(PLAYERS: list[object], player_index: int) -> None:
    """Fixes the players' index

    Args:
        PLAYERS (list[object]): Players' list
        player_index (int): The player index
    """
    if player_index == len(PLAYERS):
        player_index = 0


def check_winner(lst: list[object]) -> tuple[list[str], int]:
    """Checks who won the game

    Args:
        lst (list[object]): Players' list

    Returns:
        tuple[list[str], int]: Player's list, points
    """
    max_points = max(player._points for player in lst)
    winners = [player.name for player in lst if player._points == max_points]
    return winners, max_points


def display_winners(PLAYERS: list[object]) -> None:
    """Display the winners to the screen

    Args:
        PLAYERS (list[object]): Players' list
    """
    winners = check_winner(PLAYERS)
    time.sleep(3)
    if len(winners[0]) > 1:
        print(f"The winners are: {winners[0]}\nPoints: {winners[1]} ")
            
    else:
        print(f"The winner is: {winners[0][0]},\nPoints: {winners[1]}")
