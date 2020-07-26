#!/usr/bin/python
# Author:   @BlankGodd
# move

from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.king import King
from pieces.queen import Queen
from pieces.knight import Knight


class Move:

	def __init__(self,board):
		self.board = board
		# before every move, look if king in check
	
	# p = piece
	# y = position
	def move_pawn(self,p,y,player):
		# make the move
		piece = Pawn(self.board)
		move = piece.move(p,y,player)
		return move

	def move_rook(self,p,y,player):
		piece = Rook(self.board)
		move = piece.move(p,y,player)
		if not move:
			print('Invalid move')
		return move

	def move_bishop(self,p,y,player):
		piece = Bishop(self.board)
		move = piece.move(p,y,player)
		if not move:
			print('Invalid move')
		return move

	def move_king(self,p,y,player):
		piece = King(self.board)
		move = piece.move(p,y,player)
		if not move:
			print('Invalid move')
		return move

	def move_queen(self,p,y,player):
		piece = Queen(self.board)
		move = piece.move(p,y,player)
		if not move:
			print('Invalid move')
		return move

	def move_knight(self,p,y,player):
		piece = Knight(self.board)
		move = piece.move(p,y,player)
		if not move:
			print('Invalid move')
		return move

