#!/usr/bin/python
# Author:   @BlankGodd
# king

from pieces.positions import Pos

class King:

	def __init__(self,board):
		self.position = Pos._positions
		self.board = board
		self.alpha = Pos._alpha

	def move(self,p,ab,player):
		pass