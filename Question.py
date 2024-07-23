
class Question:
    def __init__(
        self,
        text: str,
        answers: dict[str, str],
        correct_answer: str,
        category: str,
        difficulty: str,
    ) -> None:
        """
        Constructor for Question object.

        Args:
            question (str): The text of the question.
            answers (dict[str, str]): A dictionary of answers with keys as option numbers.
            correct_answer (str): The correct answer's key.
        """
        self._text = text
        self._answers = answers
        self._correct_answer = correct_answer
        self.category = category
        self.difficulty = difficulty

    def __repr__(self) -> str:
        question_str = f"Q: {self._text}\n"
        for key, answer in self._answers.items():
            question_str += f"  {key}. {answer}\n"
        return question_str
