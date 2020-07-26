#!/usr/bin/python
# Author:   @BlankGodd
# king

from pieces.positions import Pos

class Queen:

	def __init__(self,board):
		self.position = Pos._positions
		self.board = board
		self.alpha = Pos._alpha
		
	def move(self,p,ab,player):
		a,b = self.position[ab]
		if self.board[a][b] == "  ":
			if player == 1:
				cond = self.move_white(ab, player)
				return cond
			else:
				cond = self.move_black(ab, player)
				return cond
		else:
			x = self.board[a][b]
			if player == 1:
				if x[-1] == " ":
					return False
				cond = self.white_take(ab, player)
				return cond
			else:
				if x[-1] == ".":
					return False
				cond = self.black_take(ab, player)
				return cond

	def move_white(self, ab, player):
		cond = self.check_north(ab,player)
		if not cond:
			self.check_east(ab,player)
		if not cond:
			self.check_west(ab,player)
		if not cond:
			self.check_south(ab,player)

	def check_north(self,ab,player):
		# qe3
		check = ""
		prev_pos = ""
		if player == 1:
			check = "Q "
		else:
			check = "Q."
		cond = False
		# vertical north
		alp,num = ab[0],ab[-1]
		for i in range(1,8):
			j = int(num) + 1
			if j > 8:
				break
			pos = alp + str(j)
			a,b = self.position[pos]
			if self.board[a][b] != "  ":
				if self.board[a][b] == check:
					prev_pos = pos
					cond = True
					break
				else:
					break
		if not cond:
			# north east

	