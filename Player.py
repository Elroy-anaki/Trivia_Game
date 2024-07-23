class Player:
    def __init__(self, name: str = "") -> None:

        self.name = name
        self._points = 0

    def __repr__(self) -> str:
        return f"Name: {self.name}, Points: {self._points}"

    def add_point(self) -> int:
        self._points += 1
        return self._points

    def is_correct(self, player_answer: str, correct_answer: str) -> bool:
        """
        Checks the player's answer

        Args:
            player_answer (str): Players' answer
            correct_answer (str): The correct answer of question

        Returns:
            bool: True if answered correctly, False otherwise.
        """
        if player_answer == correct_answer:

            return True
        else:
            return False

    @classmethod
    def create_players(cls, num: int) -> list["Player"]:
        """Creates players' list

        Args:
            num (int): count of players

        Returns:
            list[object]: Players' list
        """
        players = []
        for _ in range(num):
            name = input("Enter player name: ").strip().title()
            players.append(cls(name))
        return players
