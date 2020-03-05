import random
import math
import copy


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
            print('move: ', move, '  util: ', util)
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
        if win is not None: # reaches a terminal state
            return win # 1 if Player 1 wins, -1 if Player 2 wins, 0 if the board is full (indicating a tie)
        elif depth == 0: 
            return self.evaluation(state)
        if nextp == 1: # MAX is to move in state
            max_eval = -float('inf')
            for move, child in state.successors():
                util = self.minimax(child, depth) if depth is None else self.minimax(child, depth - 1)
                max_eval = max(max_eval, util)
            return max_eval
        else: # MIN is to move in state
            min_eval = float('inf')
            for move, child in state.successors():
                util = self.minimax(child, depth) if depth is None else self.minimax(child, depth - 1)
                min_eval = min(min_eval, util)
            return min_eval

    def evaluation(self, state):
        """Estimate the utility value of the game state based on features.

        N.B.: This method must run in O(1) time!

        Args:
            state: a connect4.GameState object representing the current board

        Returns: a heusristic estimate of the utility value of the state
        """

        for check in range(3, 1, -1):
            X, O = 0, 0
            # check verticals
            for c in range(7):
                for r in range(6 - check + 1):
                    val_sum = 0
                    for y in range(r, r + check):
                        val_sum += state.board[y][c]
                    if (r + check >= 6): # top space of check reaches top of the board(impossible to still have gap beneath)
                        continue
                    if abs(val_sum) == check and state.board[r + check][c] == 0: # makes sure there is an empty spot to drop
                        if val_sum > 0:
                            O += -.05*check
                        else :
                            X += .05*check  
            # check horizontals
            for r in range(6):
                for c in range(7 - check + 1):
                    val_sum = 0
                    for x in range(c, c + check):
                        val_sum += state.board[r][x]
                    if (c + check >= 7): # right side touches right edge
                        if (state.board[r][c - 1] == 0): # theres a left gap
                            if abs(val_sum) == check: 
                                if val_sum > 0:
                                    O += -.05*check
                                else :
                                    X += .05*check
                        continue
                    if (c - 1 < 0): # left side touches left edge
                        if (state.board[r][c + check] == 0): # theres a right gap
                            if abs(val_sum) == check: 
                                if val_sum > 0:
                                    O += -.05*check
                                else :
                                    X += .05*check
                        continue
                    if (abs(val_sum) == check and state.board[r][c + check] == 0) or (abs(val_sum) == check and state.board[r][c - 1] == 0):
                        if val_sum > 0:
                            O += -.05*check
                        else:
                            X += .05*check
            tot = X + O
            if tot == 0:
                continue # no matching or equal matching
            if state.next_player() == 1:
                return tot
            else:
                return -tot
        return 0 # return tie if there are no pieces in a row



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
        return self.minimax_prune_helper(state, depth, -float('inf'), float('inf'), [])

    def minimax_prune_helper(self, state, depth, alpha, beta, pruned):
        """Determine the minimax utility value the given state using alpha-beta pruning.

        N.B.: When exploring the game tree and expanding nodes, you must consider the child nodes
        in the order that they are returned by GameState.successors().  That is, you cannot prune
        the state reached by moving to column 4 before you've explored the state reached by a move
        to to column 1.

        Args: see ComputerAgent.minimax() above

        Returns: the minimax utility value of the state, along with a list of state objects that
            were not expanded due to pruning.
        """

        win = state.winner() 
        nextp = state.next_player() # whos turn it is 
        if win is not None: # reaches a terminal state
            return win, pruned # 1 if Player 1 wins, -1 if Player 2 wins, 0 if the board is full (indicating a tie)
        elif depth == 0: 
            return self.evaluation(state), pruned
        if nextp == 1: # MAX is to move in state
            max_eval = -float('inf')
            deep_successors = state.successors() 
            for move, child in state.successors():
                deep_successors.pop(0) # remove elemnt that was expanded from current successors list
                util = self.minimax_prune_helper(child, depth, alpha, beta, pruned)[0] if depth is None else self.minimax_prune_helper(child, depth - 1, alpha, beta, pruned)[0]
                max_eval = max(max_eval, util)
                alpha = max(alpha, util)
                if beta <= alpha:
                    for item in deep_successors: pruned.append(item[1]) # creates a list of only the states 
                    break
            return max_eval, pruned
        else: # MIN is to move in state
            min_eval = float('inf')
            deep_successors = state.successors() 
            for move, child in state.successors():
                deep_successors.pop(0) # remove elemnt that was expandded from current successors list
                util = self.minimax_prune_helper(child, depth, alpha, beta, pruned)[0] if depth is None else self.minimax_prune_helper(child, depth - 1, alpha, beta, pruned)[0]
                min_eval = min(min_eval, util)
                beta = min(beta, util)
                if beta <= alpha:
                    for item in deep_successors: pruned.append(item[1]) # creates a list of only the states 
                    break
            return min_eval, pruned