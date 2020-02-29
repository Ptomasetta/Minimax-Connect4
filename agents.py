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
        move__state = dict(state.successors())
        prompt = "Kindly enter your move {}: ".format(sorted(move__state.keys()))
        move = int(input(prompt))
        return move, move__state[move]


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
        
        win = state.winner() 
        nextp = state.next_player() # whos turn it is 
        if depth == 0: 
            return self.evaluation(state)
        elif win is not None: # reaches a terminal state
            return win # 1 if Player 1 wins, -1 if Player 2 wins, 0 if the board is full (indicating a tie)
        elif nextp == 1: # MAX is to move in state
            max_value = -2
            for move, child in state.successors():
                util = self.minimax(child, depth) if depth is None else self.minimax(child, depth - 1)
                max_value = max(max_value, util)
            return max_value
        else: # MIN is to move in state
            min_value = 2
            for move, child in state.successors():
                util = self.minimax(child, depth) if depth is None else self.minimax(child, depth - 1)
                min_value = min(min_value, util)
            return min_value

    def evaluation(self, state):
        """Estimate the utility value of the game state based on features.

        N.B.: This method must run in O(1) time!

        Args:
            state: a connect4.GameState object representing the current board

        Returns: a heusristic estimate of the utility value of the state
        """
        #
        # Fill this in!
        #
        return -1*state.next_player() # change


class ComputerPruneAgent(ComputerAgent):
    """Smarter computer agent that uses minimax with alpha-beta pruning to select the best move."""

    def minimax(self, state, depth):
        util, pruned = self.minimax_prune(state, depth)
        return util

    def minimax_prune(self, state, depth, alpha=-2, beta=2, pruned=[]):
        """Determine the minimax utility value the given state using alpha-beta pruning.

        N.B.: When exploring the game tree and expanding nodes, you must consider the child nodes
        in the order that they are returned by GameState.successors().  That is, you cannot prune
        the state reached by moving to column 4 before you've explored the state reached by a move
        to to column 1.

        Args: see ComputerAgent.minimax() above

        Returns: the minimax utility value of the state, along with a list of state objects that
            were not expanded due to pruning.
        """

        # added optional arguents to take care of alpha and beta
        # pruned is the list of list of state objects that were not expanded due to pruning
        
        win = state.winner() 
        nextp = state.next_player() # whos turn it is 
        if depth == 0: 
            pruned = list(dict.fromkeys(pruned))
            return self.evaluation(state), pruned
        elif win is not None: # reaches a terminal state
            pruned = list(dict.fromkeys(pruned))
            return win, pruned # 1 if Player 1 wins, -1 if Player 2 wins, 0 if the board is full (indicating a tie)
        elif nextp == 1: # MAX is to move in state
            max_value = -2
            successors = state.successors()
            for move, child in successors:
                successors.pop(0) # remove elemnt that was expandded from current successors list
                util = self.minimax_prune(child, depth, alpha, beta)[0] if depth is None else self.minimax_prune(child, depth - 1, alpha, beta)[0]
                max_value = max(max_value, util)
                alpha = max(alpha, util)
                if beta <= alpha:
                    extend_list = []
                    for item in successors: extend_list.append(item[1]) # creates a list of only the states 
                    pruned.extend(extend_list) # appends states that were not expanded to pruned
                    break
            pruned = list(dict.fromkeys(pruned)) # removes duplicates from pruned
            return max_value, pruned
        else: # MIN is to move in state
            min_value = 2
            successors = state.successors()
            for move, child in successors:
                successors.pop(0)
                util = self.minimax_prune(child, depth, alpha, beta)[0] if depth is None else self.minimax_prune(child, depth - 1, alpha, beta)[0]
                min_value = min(min_value, util)
                beta = min(beta, util)
                if beta <= alpha:
                    extend_list = []
                    for item in successors: extend_list.append(item[1]) # creates a list of only the states 
                    pruned.extend(extend_list) # appends states that were not expanded to pruned
                    break
            pruned = list(dict.fromkeys(pruned))
            return min_value, pruned