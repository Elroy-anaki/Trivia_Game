import argparse
import random
import json
import time
from Question import Question

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Trivia Game.")
    parser.add_argument('--file_path', type=str, required=True, help='Path to the JSON file with questions')
    parser.add_argument('--num_of_players', type=int, required=True, help='Number of players in the game')
    result = parser.parse_args()
    return result


def load_from_json_file_to_list(file_path: str) -> list[object]:
    with open(file_path, 'r') as f:
        questions = json.load(f)
    questions_list = []
    for question in questions["questions"]:
        q = Question(
            text=question["question"],
            answers=question["answers"],
            correct_answer=question["correct_answer"],
            category=question["category"],
            difficulty=question["difficulty"]
            
            )
        questions_list.append(q)
    return questions_list


def get_questions_categories(questions_list: list['Question']) -> set[str]:
    categories = []
    for q in questions_list:
        categories.append(q.category)
    return set(categories)


def filter_list(questions: list['Question'], category: str, difficulty: str) -> list['Question']:
    """Filters the whole questions' list to the filtered list by user choice

    Args:
        category (str): User_input
        difficulty (str): User_input
        questions (list[object]): Questions list

    Returns:
        list[object]: The filtered list of questions
    """
    filtered_list = [q for q in questions if q.category == category and q.difficulty == difficulty]
    while len(filtered_list) == 0:
        print("There is no questions in these filters.")
        category = input("Choose category again: ")
        difficulty = input("Choose difficulty level again: ")
        filtered_list = [q for q in questions if q.category == category and q.difficulty == difficulty]
    return filtered_list


def get_random_question(questions_list: list['Question']) -> Question:
    return random.choice(questions_list)
    

def valid_input(user_choose: str, options: list[str]) -> str:
    """Checks if the user choose exist in the options

    Args:
        user_choose (str): string (category or difficulty level)
        options (list[str]): list of options to choose from

    Returns:
        str: The proper user's choose 
    """
    while user_choose not in options:
        user_choose = input(f"Invalid choose, choose only from these options {options}:\n").strip().title()
        
    return user_choose


def select_filters(questions: list[object], difficulty_levels: list[str]) -> object:
    """Returns a random question during the game by user's choice

    Args:
        QUESTIONS (list[object]): Questions' list
        DIFFICULTY_LEVELS (list[str]): Difficulty levels' list

    Returns:
        object: A random question
    """
    categories = get_questions_categories(questions)
    print(f"Available categories: {categories}")
    user_category = valid_input(input("Choose category: "), categories)
    user_difficulty = valid_input(input("Choose difficulty level: "), difficulty_levels)
    corrent_list = filter_list( questions, user_category, user_difficulty)
    selected_question = get_random_question(corrent_list)
    return selected_question


def get_winner(lst: list[object]) -> tuple[list[str], int]:
    """
    Returns the winner(s) and their points 

    Args:
        lst (list[object]): Players' list

    Returns:
        tuple[list[str], int]: Player's list, points
    """
    max_points = max(player._points for player in lst)
    winners = [player.name for player in lst if player._points == max_points]
    return winners, max_points


def print_winners(PLAYERS: list[object]) -> None:
    """Display the winners to the screen

    Args:
        PLAYERS (list[object]): Players' list
    """
    winners = get_winner(PLAYERS)
    time.sleep(3)
    if len(winners[0]) > 1:
        print(f"The winners are: {winners[0]}\nPoints: {winners[1]} ")
            
    else:
        print(f"The winner is: {winners[0][0]},\nPoints: {winners[1]}")
