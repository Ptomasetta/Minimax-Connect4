import random
import math


class RandomAgent:
    """Agent that picks a random available move.  You should be able to beat it."""
    def get_move(self, state, depth=None):
        possibles = list(state.successors())
        return random.choice(possibles)


class HumanAgent:
    """Prompts user to supply a valid move."""
    def get_move(self, state, depth=None):
        move__state = state.successors()
        moves = {}
        for tup in move__state:
            moves[tup[0]] = tup[1]
        
        prompt = "Kindly enter your move {}: ".format(sorted([move[0] for move in move__state]))
        move = int(input(prompt))
        return move, moves[move]


class ComputerAgent:
    """Artificially intelligent agent that uses minimax to select the best move."""

    def get_move(self, state, depth=None):
        """Select the best available move, based on minimax value."""
        nextp = state.next_player()
        best_util = -math.inf if nextp == 1 else math.inf
        best_move = None
        best_state = None

        for move, state in state.successors():
            util = self.minimax(state, depth) 
            if ((nextp == 1) and (util > best_util)) or ((nextp == -1) and (util < best_util)):
                best_util, best_move, best_state = util, move, state
        return best_move, best_state

    def minimax(self, state, depth):
        """Determine the minimax utility value the given state.

        Args:
            state: a connect4.GameState object representing the current board
            depth: the maximum depth of the game tree that minimax should traverse before
                estimating the utility using the evaluation() function.  If depth is 0, no
                traversal is performed, and minimax returns the results of a call to evaluation().
                If depth is None, the entire game tree is traversed.

        Returns: the minimax utility value of the state
        """

        #have to deal with depth for when not None?

        win = state.winner() 
        nextp = state.next_player() # whos turn it is 

        if win is not None: # reaches a terminal state
            print("Terminl state detected: ", win)
            return win # 1 if Player 1 wins, -1 if Player 2 wins, 0 if the board is full (indicating a tie)
        elif win == 1: # MAX is to move in state
            minimax_value = -2
            for move, child in state.successors():
                util = self.minimax(child, depth) 
                minimax_value = max(minimax_value, util)
            return minimax_value
        else: # MIN is to move in state
            minimax_value = 2
            for move, child in state.successors():
                util = self.minimax(child, depth) 
                minimax_value = min(minimax_value, util)
            return minimax_value

 


        return 42  # Change this line!

    def evaluation(self, state): #zzz must be O(1)
        """Estimate the utility value of the game state based on features.

        N.B.: This method must run in O(1) time!

        Args:
            state: a connect4.GameState object representing the current board

        Returns: a heusristic estimate of the utility value of the state
        """
        #
        # Fill this in!
        #
        return 19  # Change this line!


class ComputerPruneAgent(ComputerAgent):
    """Smarter computer agent that uses minimax with alpha-beta pruning to select the best move."""

    def minimax(self, state, depth):
        util, pruned = self.minimax_prune(state, depth)
        return util

    def minimax_prune(self, state, depth):
        """Determine the minimax utility value the given state using alpha-beta pruning.

        N.B.: When exploring the game tree and expanding nodes, you must consider the child nodes
        in the order that they are returned by GameState.successors().  That is, you cannot prune
        the state reached by moving to column 4 before you've explored the state reached by a move
        to to column 1.

        Args: see ComputerAgent.minimax() above

        Returns: the minimax utility value of the state, along with a list of state objects that
            were not expanded due to pruning.
        """
        #
        # Fill this in!
        #
        return 44, []  # Change this line!


