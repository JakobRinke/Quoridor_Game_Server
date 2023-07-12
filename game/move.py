from game.board import *
from game.util import *

class Move:
    def is_valid(self, board:GameState):
        pass


class PawnMove(Move):
    def __init__(self, start:Vector, to:Vector, player:Player):
        super.__init__()
        self.start = start
        self.to = to
        self.player = player

    def is_valid(self, board:GameState):
        if self.player.position != board.get_current_player().position:
            return False
        if len(self.start - self.to) == 1:
            return board.can_go(self.start, self.to)




class WallMove(Move):
    def __init__(self, wall:Wall):
        self.wall = wall

    def is_valid(self, board:GameState):
        pass

