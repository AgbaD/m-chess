#!/usr/bin/python
# Author:   @BlankGodd
# knight

from pieces.positions import Pos

class Knight:

	def __init__(self,board):
		self.position = Pos._positions
		self.board = board
		self.alpha = Pos._alpha

    def move(self,p,ab,player):
        pass