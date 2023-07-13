from quoridor import *
from quoridor.move import *

class Player:
    def __init__(self, position:Vector, name:str, wall_num:int, goal:int):
        self.position = position
        self.name = name
        self.wall_num = wall_num
        self.opponent = None
        self.goal = goal


class GameState:
    def __init__(self, player1_name="Player1", player2_name="Player2", walls=10):
        self.player1 = Player(Vector(4, 0), player1_name, walls, 8)
        self.player2 = Player(Vector(4, 8), player2_name, walls, 0)
        self.player1.opponent = self.player2
        self.player2.opponent = self.player1
        self.turn = 1
        self.walls:list[Wall] = []

    def _get_current_player_trn(self):
        return 2 - self.turn % 2

    def get_current_player(self):
        if self._get_current_player_trn() == 1:
            return self.player1
        return self.player2

    def can_go(self, frm:Vector, to:Vector):
        return len([wall for wall in self.walls if wall.blocks(frm, to)]) == 0

    def get_wall_moves(self):
        wall_moves:list[Move] = []
        for x in range(8):
            for y in range(8):
                if self.can_go(Vector(x, y), Vector(x+1, y))  and \
                    self.can_go(Vector(x, y+1), Vector(x+1, y+1)):



    def get_possible_moves(self, player:Player):
        moves:list[Move] = []


    def get_current_possible_moves(self):
        return self.get_possible_moves(self.get_current_player())