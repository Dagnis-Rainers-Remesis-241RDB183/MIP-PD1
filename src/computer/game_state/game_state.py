class GameState:
    @staticmethod
    def create(numbers: list[int] | str, p1: int = 0, p2: int = 0) -> str:
        state = str(p1) + "|"

        if isinstance(numbers, list):
            for num in numbers:
                state += str(num)
        else:
            state += numbers

        state += "|" + str(p2)

        return state
