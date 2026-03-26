class Node:
    children: list[str]
    parent: str | None
    selection: int
    evaluation: float | None

    def __init__(self, parent: str | None = None, selection: int = 0):
        self.children = []
        self.parent = parent
        self.selection = selection
        self.evaluation = None
