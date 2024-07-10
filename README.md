# Trivia Game

## Overview
The Trivia Game is a multiplayer quiz game where players take turns answering questions. Points are awarded for correct answers, and the game continues until all questions have been answered. The player with the most points at the end of the game wins.

## Knowledge Required
In addition to the knowledge from previous classes, the following is required:
- Classes
- JSON files and parsing
- Some understanding of Pydantic for extra features
- Some understanding of exceptions
- Possibly requests for extra features

## Required Packages
The necessary packages for this exercise include built-in ones and optional extras:
- Required:
  - argparse
  - random
  - json
- Extra:
  - pydantic

## Core Functionality

1. The game selects a question unknown to both players and displays it with all possible answers (each answer is numbered).
2. Players take turns answering the question:
   - If the answer is correct, the player earns a point.
   - If the answer is incorrect, the game notifies the player.
3. The next player then takes their turn:
   - If the previous player answered correctly, a new question is presented.
   - If the previous player answered incorrectly, the same question is presented.

## Full Requirements

- The game runs from the command line using `argparse` or a similar library.
- Parameters:
  - Path to the file with the questions list.
  - Number of players.
- Game Flow:
  - The computer selects a question from the file.
  - Players take turns answering the question as described in the Core Functionality section.
  - Correct answers earn points, and the next player gets a new question.
  - Incorrect answers prompt the same question for the next player.
  - The game ends when there are no more questions, and the winner and full scores are displayed.

- Questions:
  - The order of questions should be different each game.
  - The order of answers for each question should be different each game.

## Extra Features

- Categories and Difficulty Levels:
  - Each question has a category and difficulty level (easy, medium, hard).
  - Players can choose a category and difficulty level before a new question is asked.
  - The game selects a question from the chosen category and difficulty level.
  - The game should ensure only available categories and difficulty levels can be chosen.
  
- Web API for Questions:
  - Fetch questions from a web API instead of a file.

## Usage

To start the game, use the following command:

```bash
python trivia_game.py --questionlist path/to/questions.json --players int
