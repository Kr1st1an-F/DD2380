#!/usr/bin/env python3
from fishing_game_core.game_tree import Node
from fishing_game_core.player_utils import PlayerController
from fishing_game_core.shared import ACTION_TO_STR


class PlayerControllerMinimax(PlayerController):

    def __init__(self):
        super(PlayerControllerMinimax, self).__init__()

    def player_loop(self):
        first_msg = self.receiver()

        while True:
            msg = self.receiver()

            node = Node(message=msg, player=0)

            best_move = self.search_best_next_move(initial_tree_node=node)

            self.sender({"action": best_move, "search_time": None})

    def search_best_next_move(self, initial_tree_node):

        best_move = self.minimax(initial_tree_node, depth=3)
        return ACTION_TO_STR[best_move]

    def minimax(self, node, depth):

        best_move = None
        best_value = float('-inf')

        for child in node.compute_and_get_children():
            value = self.min_value(child, depth - 1, float('-inf'), float('inf'))
            if value > best_value:
                best_value = value
                best_move = child.move

        return best_move

    def max_value(self, node, depth, alpha, beta):
        if depth <= 0 :
            return self.heuristic(node)

        value = float('-inf')
        for child in node.compute_and_get_children():
            value = max(value, self.min_value(child, depth - 1, alpha, beta))
            alpha = max(alpha, value)
            if beta <= alpha:
                break

        return value

    def min_value(self, node, depth, alpha, beta):
        if depth >= 3 :
            return self.heuristic(node)

        value = float('inf')
        for child in node.compute_and_get_children():
            value = min(value, self.max_value(child, depth - 1, alpha, beta))
            beta = min(beta, value)
            if beta <= alpha:
                break

        return value

    def heuristic(self, node):
        # Simple heuristic function reflecting key game aspects
        player_score = node.state.player_scores[0]
        opponent_score = node.state.player_scores[1]

        return player_score - opponent_score
