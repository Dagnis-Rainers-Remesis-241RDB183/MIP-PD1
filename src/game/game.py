import random


class Game:
    numbers: list[int]
    selection: int
    playerScore: int
    computerScore: int

    def __init__(self) -> None:
        self.numbers = self._generate_numbers(25)
        self.selection = 0
        self.playerScore = 0
        self.computerScore = 0

    def _generate_numbers(self, count: int) -> list[int]:
        numbers: list[int] = []

        for _ in range(count):
            number = random.randint(1, 6)
            numbers.append(number)

        return numbers

    def move_left(self) -> None:
        self.selection = max(0, self.selection - 1)

    def move_right(self) -> None:
        self.selection = min(len(self.numbers) - 2, self.selection + 1)

    def select(self) -> None:
        _a = self.numbers.pop(self.selection)
        _b = self.numbers.pop(self.selection)
        self.selection = min(len(self.numbers) - 2, self.selection)
