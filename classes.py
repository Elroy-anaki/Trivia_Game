
class Player:
    def __init__(self, name: str = "") -> None:
        """
        Constructor for Player object.
        
        Args:
            name (str): The name of the player.
        """
        self.name = name
        self._points = 0
        
        
    def __repr__(self) -> str:
        """
        String representation of the Player object.
        
        Returns:
            str: String representing the player's name and points.
        """
        return f"Name: {self.name}, Points: {self._points}"
    
    
    def add_point(self) -> int:
        """
        Add a point to the player's score.
        
        Returns:
            int: The updated points of the player.
        """
        self._points += 1
        return self._points
    
    
    def check_answer(self, player_answer: str, correct_answer: str) -> bool:
        """Checks the player's answer and gives him a point if he answered correctly

        Args:
            player_answer (str): Players' answer
            correct_answer (str): The correct answer of question 

        Returns:
            bool: True if answered correctly, False otherwide.
        """
        if player_answer == correct_answer:
            self.add_point()
            return True
        else:
            return False
    
    
    @classmethod
    def create_players(cls, num: int) -> list[object]:
        """Creates players' list

        Args:
            num (int): count of players

        Returns:
            list[object]: Players' list
        """
        players = []
        for i in range(num):
            name = input("Enter player name: ").strip().title()
            players.append(cls(name))
        return players
    
    
    
class Question:
    def __init__(self, question: str, answers: dict[str, str], correct_answer: str, category: str, difficulty: str) -> None:
        """
        Constructor for Question object.
        
        Args:
            question (str): The text of the question.
            answers (dict[str, str]): A dictionary of answers with keys as option numbers.
            correct_answer (str): The correct answer's key.
        """
        self._question = question
        self._answers = answers
        self._correct_answer = correct_answer
        self.category = category
        self.difficulty = difficulty
        
        
    def __repr__(self) -> str:
        """
        String representation of the Question object.
        
        Returns:
            str: String representing the question and its possible answers.
        """
        question_str = f"Q: {self._question}\n"
        for key, answer in self._answers.items():
            question_str += f"  {key}. {answer}\n"
        return question_str
