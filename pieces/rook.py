#!/usr/bin/python
# Author:   @BlankGodd
# rook

from pieces.positions import Pos

class Rook:

	def __init__(self,board):
		self.position = Pos._positions
		self.board = board
		self.alpha = Pos._alpha

	def move(self,p,ab,player):
		a,b = self.position[ab]
		if self.board[a][b] == '  ':
			if player == 1: #white
				cond = self.move_white(ab,player)
				return cond
			else: # black
				cond = self.move_black(ab,player)
				return cond
		else:
			if player == 1: #white
				x = self.board[a][b]
				if x[-1] == ' ':
					return False
				cond = self.white_take(ab,player)
				return cond
			else: # black
				x = self.board[a][b]
				if x[-1] == '.':
					return False
				cond = self.black_take(ab,player)
				return cond
			
	def white_take(self,ab,player):
		cond = self.check_vert(ab,player)
		if not cond:
			cond = self.check_hori(ab,player)
		if cond:
			a,b = self.position[ab]
			c,d = self.position[cond]
			self.board[a][b] = 'R '
			self.board[c][d] = '  '
			print('R{}x{}'.format(cond,ab))
			return True
		return cond

	def black_take(self,ab,player):
		cond = self.check_vert(ab,player)
		if not cond:
			cond = self.check_hori(ab,player)
		if cond:
			a,b = self.position[ab]
			c,d = self.position[cond]
			self.board[a][b] = 'R.'
			self.board[c][d] = '  '
			print('R.{}x{}'.format(cond,ab))
			return True
		return cond

	def move_white(self,ab,player):
		cond = self.check_vert(ab,player)
		if not cond:
			cond = self.check_hori(ab,player)
		if cond:
			a,b = self.position[ab]
			c,d = self.position[cond]
			self.board[a][b] = 'R '
			self.board[c][d] = '  '
			return True
		return cond

	def move_black(self,ab,player):
		cond = self.check_vert(ab,player)
		if not cond:
			cond = self.check_hori(ab,player)
		if cond:
			a,b = self.position[ab]
			c,d = self.position[cond]
			self.board[a][b] = 'R.'
			self.board[c][d] = '  '
			return True
		return cond

	def check_hori(self,ab,player):
		check = ''
		if player == 1:
			check = 'R '
		else:
			check = 'R.'
		num = ab[-1]
		alp = ab[0]
		alp = self.alpha[alp]
		cond = False
		for i in range(1,8):
			j = alp-i
			if j < 1:
				break
			j = self.alpha[j]
			pos = j+num
			a,b = self.position[pos]
			if self.board[a][b] != "  ":
				if self.board[a][b] == check:
					prev_pos = pos
					cond = True
					break
				else:
					break
		if not cond:
			for i in range(1,8):
				j = alp+i
				if j > 8:
					break
				j = self.alpha[j]
				pos = j+num
				a,b = self.position[pos]
				if self.board[a][b] != "  ":
					if self.board[a][b] == check:
						prev_pos = pos
						cond = True
						break
					else:
						break
		if cond:
			return prev_pos
		return cond

	def check_vert(self,ab,player):
		check = ''
		if player == 1:
			check = 'R '
		else:
			check = 'R.'
		alp = ab[0]
		num = ab[-1]	#8
		num = int(num)
		cond = False
		prev_pos = ""
		for i in range(1,8):
			j = num-i
			if j < 1:
				break
			j = str(j)
			pos = alp+j
			a,b = self.position[pos]
			if self.board[a][b] != '  ':
				if self.board[a][b] == check:
					prev_pos = pos
					cond = True
					break
				else:
					break
		if not cond:
			for i in range(1,8):
				j = num+i
				if j > 8:
					break
				j = str(j)
				pos = alp+j
				a,b = self.position[pos]
				if self.board[a][b] != '  ':
					if self.board[a][b] == check:
						prev_pos = pos
						cond = True
						break
					else:
						break
		if cond:
			return prev_pos
		return cond
			

