from quoridor.board import *
from quoridor.util import *


class Move:
    def is_valid(self, board: GameState) -> bool:
        return False


class PawnMove(Move):
    def __init__(self, start: Vector, to: Vector, player: Player):
        super.__init__()
        self.start = start
        self.to = to
        self.player = player

    def is_valid(self, board: GameState) -> bool:
        if self.player.position != board.get_current_player().position:
            return False
        if len(self.start - self.to) == 1:
            return board.can_go(self.start, self.to)

        v_dir = self.player.position - self.player.opponent.position
        if len(v_dir) != 1 or not board.can_go(self.start, self.player.opponent.position):
            return False

        if self.player.opponent.position + v_dir == self.to:
            return board.can_go(self.player.opponent.position, self.to)

        s_dir = v_dir.switched()
        if self.player.opponent.position + s_dir == self.to:
            return board.can_go(self.player.opponent.position, self.to)

        return False


class WallMove(Move):
    def __init__(self, wall: Wall, player: Player):
        self.wall = wall
        self.player = player

    def is_valid(self, board: GameState) -> bool:
        if self.player.wall_num < 1:
            return False
        for board_wall in board.walls:
            if board_wall.blocks(self.wall.pbs1, self.wall.pbe1) or \
                    board_wall.blocks(self.wall.pbs2, self.wall.pbe2):
                return False
            if board_wall.blocks(self.wall.pbs1, self.wall.pbs2) and \
                    board_wall.blocks(self.wall.pbe1, self.wall.pbe2):
                return False
        return True
