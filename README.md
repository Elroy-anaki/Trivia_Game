# Trivia Game

## Knowledge Required

In addition to the knowledge from previous classes, the following is required:

- **Classes**
- **JSON files and parsing**
- Some understanding of **pydantic** for the extra features
- Some understanding of **exceptions**
- Maybe **requests** for the extra features

## Packages Required

Most of the packages used for this exercise are built-in, and not all of them have to be used.

### Required Packages

- argparse
- random
- json

### Extra Packages

- pydantic

## Things to Go Over in the Lecture

- Classes and objects
- Classes vs data structures (records)
- Exceptions
- Sets
- JSON files

### Extra

- pydantic for data validation and parsing - extra

## The Exercise

It is recommended to first implement the core functionality of the game, then do the full requirements and then add the extra features.

### Core Functionality

The basic idea of the game is to have a trivia questions game. If we have 2 players playing, then the game would go like this:

- The game selects a question that is unknown to both of the players, and then prints the question with all the possible answers (each answer with a number).
- The players take turns answering the question.
- If the answer is correct, the player gets a point.
- If the answer is wrong, the game prints a message saying that the answer is wrong.
- In either case, the turn goes to the next player. If the previous player answered correctly, the next player gets a new question; if not, they get the same question, with the same answers.

So, if a question was not answered correctly, the next player gets the same question, with the same answers, and has a greater chance of answering correctly.

### Full Requirements

The game should be activated from the command line (using argparse, or something similar).

#### Parameters

- Path to the file with the question list
- Number of players

The computer selects a question from the file, and the players take turns answering the question as described in the Core Functionality section.

- If the current player answers correctly, they get a point, and the next player gets a new question.
- If the current player answers incorrectly, the next player gets the same question, with the same answers.
- When there are no more questions, the game is finished, and should print the winner and the full scores.

If the game is played twice with the same file:

- The order of the questions should be different each time.
- The order of the answers in each question should be different each time (each game, not each time the question is asked).

### Extra Features

- Allow categories and difficulty levels (and allow choosing).

#### Implementation

- Each question has a category (you decide them) and a difficulty level (easy, medium, hard).
- On each turn, before a new question is asked, the player can choose a category and a difficulty level from the ones still available.
- The game should then select a question from the selected category and difficulty level (if there is more than one question in that category and difficulty level, the program chooses one of them at random).
- The computer should not allow choosing a category and difficulty level that are not available.

- Get the questions from a web API instead of a file.
