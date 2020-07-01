#!/usr/bin/python
# Author:   @BlankGodd
# bishop

from pieces.positions import Pos

class Bishop:

	def __init__(self,board):
		self.position = Pos._positions
		self.board = board
		self.alpha = Pos._alpha

	def move(self,p,ab,player):
		a,b = self.position[ab]
		if self.board[a][b] == '  ':
			if player == 1:
				m = self.move_white(ab,player)
				return m
			else:
				m = self.move_black(ab,player)
				return m
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
		mode = self.check_left(ab,player)
		if not mode:
			mode = self.check_right(ab,player)
		if mode:
			a,b = self.position[ab]
			c,d = self.position[mode]
			self.board[a][b] = 'B '
			self.board[c][d] = '  '
			print('B{}x{}'.format(mode,ab))
			return True
		return mode

	def black_take(self,ab,player):
		mode = self.check_left(ab,player)
		if not mode:
			mode = self.check_right(ab,player)
		if mode:
			a,b = self.position[ab]
			c,d = self.position[mode]
			self.board[a][b] = 'B.'
			self.board[c][d] = '  '
			print('B.{}x{}'.format(mode,ab))
			return True
		return mode

	def move_white(self,ab,player):
		mode = self.check_left(ab,player)
		if not mode:
			mode = self.check_right(ab,player)
		if mode:
			a,b = self.position[ab]
			c,d = self.position[mode]
			self.board[a][b] = 'B '
			self.board[c][d] = '  '
			return True
		return mode

	def move_black(self,ab,player):
		mode = self.check_left(ab,player)
		if not mode:
			mode = self.check_right(ab,player)
		if mode:
			a,b = self.position[ab]
			c,d = self.position[mode]
			self.board[a][b] = 'B.'
			self.board[c][d] = '  '
			return True
		return mode

	def check_right(self,ab,player):
		check = ""
		prev_pos = ''
		if player == 1:
			check = 'B '
		else:
			check = 'B.'
		alp = ab[0]
		num = int(ab[-1])
		l = self.alpha[alp]
		cond = False
		for i in range(1,8):
			j = num-i
			if j < 1:
				break
			k = l+i
			if k > 8:
				break
			k = self.alpha[k]
			pos = k+str(j)
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
				k = l+i
				if k > 8:
					break
				k = self.alpha[k]
				pos = k+str(j)
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

	def check_left(self,ab,player):
		check = ""
		prev_pos = ''
		if player == 1:
			check = 'B '
		else:
			check = 'B.'
		alp = ab[0]
		num = int(ab[-1])
		l = self.alpha[alp]
		cond = False
		for i in range(1,8):
			j = num-i
			if j < 1:
				break
			k = l-i
			if k < 1:
				break
			k = self.alpha[k]
			pos = k+str(j)
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
				k = l-i
				if k < 1:
					break
				k = self.alpha[k]
				pos = k+str(j)
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

