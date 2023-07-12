from game.util import *


class Player:
    def __init__(self, position:Vector, name:str, wall_num:int):
        self.position = position
        self.name = name
        self.wall_num = wall_num


class GameState:
    def __init__(self, player1_name="Player1", player2_name="Player2", walls=10):
        self.player1 = Player(Vector(4, 0), player1_name, walls)
        self.player2 = Player(Vector(4, 8), player2_name, walls)
        self.turn = 1
        self.walls: [Wall] = []

    def _get_current_player_trn(self):
        return 2 - self.turn % 2

    def get_current_player(self):
        if self._get_current_player_trn() == 1:
            return self.player1
        return self.player2

    def can_go(self, frm:Vector, to:Vector):
        return len([wall for wall in self.walls if wall.blocks(frm, to)]) == 0

