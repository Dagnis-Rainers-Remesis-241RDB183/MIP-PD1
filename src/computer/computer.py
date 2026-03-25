import json

from typing_extensions import Any

from .game_state import GameState
from .node import Node


class Computer:
    algorithm: bool
    root_game_state: str
    computer_start: bool
    thinking: bool
    tree: dict[str, Node]
    json_tree: dict[str, Any]
    max_level: int

    def __init__(
        self,
        computer_start: bool = False,
        numbers: list[int] = [],
        max_level: int = 1,
        algorithm: bool = False,
    ):
        self.computer_start = computer_start
        self.root_game_state = GameState.create(numbers)
        self.thinking = False
        self.tree = {}
        self.json_tree = {}
        self.max_level = max_level
        self.algorithm = algorithm

    def create_tree(self, game_state: str, level: int = 0) -> None:
        if level + 1 > self.max_level:
            return

        node = self.tree.get(game_state)

        if node is None:
            node = Node()
            self.tree[game_state] = node

        if len(node.children) == 0:
            self.create_nodes(game_state)

        for child in node.children:
            self.create_tree(child, level + 1)

    def get_best_action(self, game_state: str) -> str:
        node: Node = self.tree[game_state]

        best_val = -float("inf")
        id = 0

        for i, child in enumerate(node.children):
            current_move_val = -float("inf")

            if self.algorithm:
                current_move_val = self.alfa_beta(child, True)
            else:
                current_move_val = self.min_max(child, True)

            if current_move_val > best_val:
                best_val = current_move_val
                id = i

        return node.children[id]

    # Izveidota HNF
    def heuristic_function(self, game_state: str) -> float:
        p1, _number_row, p2 = self.extract_game_state(game_state)
        computer_score: int
        player_score: int

        if self.computer_start:
            computer_score = p1
            player_score = p2
        else:
            computer_score = p2
            player_score = p1

        result = computer_score - player_score

        return float(result)

    def check_if_end(self, game_state: str) -> bool:
        p1, current_row, p2 = self.extract_game_state(game_state)

        if len(current_row) == 1:
            if p1 > p2:
                if self.computer_start:
                    return True
            elif p1 < p2:
                if not self.computer_start:
                    return True

        return False

    def extract_game_state(self, game_state: str) -> tuple[int, str, int]:
        result = game_state.split("|")
        return int(result[0]), result[1], int(result[2])

    def create_nodes(self, game_state: str) -> None:
        node: Node = self.tree[game_state]

        current_p1, current_row, current_p2 = self.extract_game_state(game_state)
        current_distance = len(current_row)

        if current_distance == 1:
            return

        _root_p1, root_row, _root_p2 = self.extract_game_state(self.root_game_state)
        root_distance = len(root_row)
        turns_played = root_distance - current_distance

        p1_turn = turns_played % 2 == 0

        for i in range(0, current_distance - 1, 2):
            p1 = current_p1
            p2 = current_p2
            a = int(current_row[i])
            b = int(current_row[i + 1])
            sum = a + b

            add_points = 0
            if sum > 6:
                sum -= 6
                add_points = sum

            next_row = current_row[:i] + str(sum) + current_row[i + 2 :]

            if p1_turn:
                p1 += add_points
            else:
                p2 += add_points

            new_state = GameState.create(next_row, p1, p2)
            node.children.append(new_state)
            new_node = Node(game_state, i)
            self.tree[new_state] = new_node

        if current_distance % 2 != 0:
            p1 = current_p1
            p2 = current_p2

            new_row = current_row[:-1]

            if p1_turn:
                p2 -= 1
            else:
                p1 -= 1

            new_state = GameState.create(new_row, p1, p2)
            node.children.append(new_state)
            new_node = Node(game_state, current_distance - 1)
            self.tree[new_state] = new_node

    def min_max(self, game_state: str, maximizing: bool) -> float:
        node: Node = self.tree[game_state]

        _, number_row, _ = self.extract_game_state(game_state)

        if len(node.children) == 0 or len(number_row) <= 1:
            return self.heuristic_function(game_state)

        if maximizing:
            best_val = -float("inf")
            for child in node.children:
                val = self.min_max(child, False)
                best_val = max(best_val, val)
            return best_val
        else:
            best_val = float("inf")
            for child in node.children:
                val = self.min_max(child, True)
                best_val = min(best_val, val)
            return best_val

    def alfa_beta(self, game_state: str, maximizing: bool) -> float:
        node: Node = self.tree[game_state]

        _, number_row, _ = self.extract_game_state(game_state)

        if len(node.children) == 0 or len(number_row) <= 1:
            return self.heuristic_function(game_state)

        if maximizing:
            best_val = -float("inf")
            for child in node.children:
                val = self.min_max(child, False)
                best_val = max(best_val, val)
                if best_val >= 1:
                    break

            return best_val
        else:
            best_val = float("inf")
            for child in node.children:
                val = self.min_max(child, True)
                best_val = min(best_val, val)
                if best_val <= -1:
                    break

            return best_val

    def print_tree(self, game_state: str):
        self.json_tree = {game_state: {}}
        self.build_json_tree(game_state, self.json_tree[game_state])

        jt = json.dumps(self.json_tree, indent=4)

        with open("tree.json", "w") as f:
            _ = f.write(jt)

    def build_json_tree(self, parent: str, upper_dict: dict[str, Any]):
        for child in self.tree[parent].children:
            upper_dict[child] = {
                "minmax": self.min_max(parent, self.computer_start),
                "heuristic": self.heuristic_function(child),
            }
            self.build_json_tree(child, upper_dict[child])

    def action(self, numbers: list[int], p1: int = 0, p2: int = 0) -> int:
        game_state = GameState.create(numbers, p1, p2)
        self.create_tree(game_state)
        action = self.get_best_action(game_state)
        self.print_tree(game_state)
        return self.tree[action].selection
