#!/usr/bin/python
# Author:   @BlankGodd
# king

from pieces.positions import Pos

class King:

	def __init__(self,board):
		self.position = Pos._positions
		self.board = board
		self.alpha = Pos._alpha
		# kd2
		# p = k
		# ab = d2

	def move(self,p,ab,player):
		a,b = self.position[ab]
		if self.board[a][b] == "  ":
			if player == 1: # white
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
				cond = self.white_take(ab,player)
				return cond
			else:
				if x[-1] == ".":
					return False
				cond = self.black_take(ab,player)
				return cond

	def white_take(self,ab,player):
		cond = self.check_round(ab, player)
		if not cond:
			cond = self.check_diag(ab, player)
		if not cond:
			return cond
		a,b = self.position[ab]
		c,d = self.position[cond]
		self.board[a][b] = "K "
		self.board[c][d] = "  "
		print("K{}x{}".format(cond,ab))
		return True

	def black_take(self,ab,player):
		cond = self.check_round(ab, player)
		if not cond:
			cond = self.check_diag(ab, player)
		if not cond:
			return cond
		a,b = self.position[ab]
		c,d = self.position[cond]
		self.board[a][b] = "K."
		self.board[c][d] = "  "
		print("K.{}x{}".format(cond,ab))
		return True

	def move_black(self, ab, player):
		cond = self.check_round(ab, player)
		if not cond:
			cond = self.check_diag(ab, player)
		if not cond:
			return cond
		a,b = self.position[ab]
		c,d = self.position[cond]
		self.board[a][b] = "K."
		self.board[c][d] = "  "
		return True

	def move_white(self, ab, player):
		cond = self.check_round(ab, player)
		if not cond:
			cond = self.check_diag(ab, player)
		if not cond:
			return cond
		a,b = self.position[ab]
		c,d = self.position[cond]
		self.board[a][b] = "K "
		self.board[c][d] = "  "
		return True

	def check_round(self,ab,player):
		check = ""
		prev_pos = ""
		if player == 1:
			check = "K "
		else:
			check = "K."
		cond = False
		x,y = ab[0],ab[1]
		y = int(y)-1
		if y < 1:
			return False
		pos = x+str(y)
		a,b = self.position[pos]
		if self.board[a][b] == check:
			cond = True
			prev_pos = pos
		if not cond:
			x,y = ab[0],ab[1]
			y = int(y)+1
			if y > 8:
				return False
			pos = x+str(y)
			a,b = self.position[pos]
			if self.board[a][b] == check:
				cond = True
				prev_pos = pos
		if not cond:
			x,y = ab[0],ab[1]
			n = self.alpha[x]
			n = n-1
			if n < 1:
				return False
			x = self.alpha[n]
			pos = x+y
			a,b = self.position[pos]
			if self.board[a][b] == check:
				cond = True
				prev_pos = pos
		if not cond:
			x,y = ab[0],ab[1]
			n = self.alpha[x]
			n = n+1
			if n > 8:
				return False
			x = self.alpha[n]
			pos = x+y
			a,b = self.position[pos]
			if self.board[a][b] == check:
				cond = True
				prev_pos = pos
		
		if cond:
			return prev_pos
		return cond
		
	def check_diag(self,ab,player):
		# check diagonally from the point
		check = ""
		prev_pos = ""
		if player == 1:
			check = "K "
		else:
			check = "K."
		cond = False
		x,y = ab[0],ab[1]
		n = self.alpha[x]
		n -= 1
		if n < 1:
			return False
		x = self.alpha[n]
		y = int(y)-1
		if y < 1:
			return False
		pos = x+str(y)
		a,b = self.position[pos]
		if self.board[a][b] == check:
			cond = True
			prev_pos = pos
		if not cond:
			x,y = ab[0],ab[1]
			n = self.alpha[x]
			n -= 1
			if n < 1:
				return False
			x = self.alpha[n]
			y = int(y)+1
			if y > 8:
				return False
			pos = x+str(y)
			a,b = self.position[pos]
			if self.board[a][b] == check:
				cond = True
				prev_pos = pos
		if not cond:
			x,y = ab[0],ab[1]
			n = self.alpha[x]
			n += 1
			if n > 8:
				return False
			x = self.alpha[n]
			y = int(y)-1
			if y < 1:
				return False
			pos = x+str(y)
			a,b = self.position[pos]
			if self.board[a][b] == check:
				cond = True
				prev_pos = pos
		if not cond:
			x,y = ab[0],ab[1]
			n = self.alpha[x]
			n += 1
			x = self.alpha[n]
			y = int(y)+1
			pos = x+str(y)
			a,b = self.position[pos]
			if self.board[a][b] == check:
				cond = True
				prev_pos = pos

		if cond:
			return prev_pos
		return cond

