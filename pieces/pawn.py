#!/usr/bin/python
# Author:   @BlankGodd
# moving pawn

# one more thing to write
# when a pawn gets to the extreme end, it changes

from pieces.positions import Pos

class Pawn:	

	def __init__(self,board):
		self.position = Pos._positions
		self.board = board
		self.alpha = Pos._alpha

	def move(self,p,ab,player):
		a,b = self.position[ab]
		val = ab[0]
		m = False
		num = int(ab[-1])
		if self.board[a][b] == "  ":
			if player == 1:
				if num < 2:
					return False
				ini = self.check_ini_white(val)
				if ini:
					m = self.move_white_ini(ab)
				else:
					m = self.move_white(ab)
			else:
				if num > 7:
					return False
				ini = self.check_ini_black(val)
				if ini:
					m = self.move_black_ini(ab)
				else:
					m = self.move_black(ab)
		else:
			if player == 1:
				if num < 2:
					return False
				m = self.white_take_piece(ab)
			else:
				if num > 7:
					return False
				m = self.black_take_piece(ab)
		return m

	def white_take_piece(self,ab):
		prev_pos = ""
		cond = False
		n = int(ab[-1])
		n -= 1
		n = str(n)

		m = ab[0]
		m = self.alpha[m]
		try:
			m_ = m - 1
			m = self.alpha[m_]
			pos = m + n
			a,b = self.position[pos]
			if self.board[a][b] == 'p ':
				prev_pos = pos
				cond = True
		except:
			pass
		m = ab[0]
		m = self.alpha[m]
		if not cond:
			m_ = m + 1
			m = self.alpha[m_]
			pos = m + n
			a,b = self.position[pos]
			if self.board[a][b] == 'p ':
				prev_pos = pos
				cond = True
		if cond:
			a,b = self.position[ab]
			c,d = self.position[prev_pos]
			self.board[a][b] = 'p '
			self.board[c][d] = '  '
			print('p{}x{}'.format(prev_pos,ab))
		else:
			print('Invalid move')
		return cond

	def black_take_piece(self,ab):
		prev_pos = ""
		cond = False
		n = int(ab[-1])
		n += 1
		n = str(n)

		m = ab[0]
		m = self.alpha[m]
		try:
			m_ = m - 1
			m = self.alpha[m_]
			pos = m + n
			a,b = self.position[pos]
			if self.board[a][b] == 'p.':
				prev_pos = pos
				cond = True

		except:
			pass
		m = ab[0]
		m = self.alpha[m]
		if not cond:
			m_ = m + 1
			m = self.alpha[m_]
			pos = m + n
			a,b = self.position[pos]
			if self.board[a][b] == 'p.':
				prev_pos = pos
				cond = True
		if cond:
			a,b = self.position[ab]
			c,d = self.position[prev_pos]
			self.board[a][b] = 'p.'
			self.board[c][d] = '  '
			print('p.{}x{}'.format(prev_pos,ab))
		else:
			print('Invalid move')
		return cond

	def move_white(self,ab):
		prev_pos = ""
		cond = False
		n = int(ab[-1])
		n -= 1
		n = str(n)
		pos = ab[0] + n
		a,b = self.position[pos]
		if self.board[a][b] == 'p ':
			prev_pos = pos
			cond = True
		if cond:
			a,b = self.position[ab]
			c,d = self.position[prev_pos]
			self.board[a][b] = 'p '
			self.board[c][d] = '  '
		else:
			print('Invalid move')
		return cond

	def move_black(self,ab):
		prev_pos = ""
		cond = False
		n = int(ab[-1])
		n += 1
		n = str(n)
		pos = ab[0] + n
		a,b = self.position[pos]
		if self.board[a][b] == 'p.':
			prev_pos = pos
			cond = True
		if cond:
			a,b = self.position[ab]
			c,d = self.position[prev_pos]
			self.board[a][b] = 'p.'
			self.board[c][d] = '  '
		else:
			print('Invalid move')
		return cond

	def check_ini_white(self,val):
		x = '2'
		v = val+x
		a,b = self.position[v]
		if self.board[a][b] == 'p ':
			return True
		return False

	def check_ini_black(self,val):
		x = '7'
		v = val+x
		a,b = self.position[v]
		if self.board[a][b] == 'p.':
			return True
		return False

	def move_white_ini(self,ab):
		# ab = b3
		prev_pos = ""
		cond = False
		n = int(ab[-1])
		for i in range(1,3):
			j = n-i
			j = str(j)
			pos = ab[0] + j
			a,b = self.position[pos]
			if self.board[a][b] == 'p ':
				prev_pos = pos
				cond = True
				break
		if cond:
			a,b = self.position[ab]
			c,d = self.position[prev_pos]
			self.board[a][b] = 'p '
			self.board[c][d] = '  '
		else:
			print('Invalid move')
		return cond

	def move_black_ini(self,ab):
		# ab = b3
		prev_pos = ""
		cond = False
		n = int(ab[-1])
		for i in range(1,3):
			j =n+i
			j = str(j)
			pos = ab[0] + j
			a,b = self.position[pos]
			if self.board[a][b] == 'p.':
				prev_pos = pos
				cond = True
				break
		if cond:
			a,b = self.position[ab]
			c,d = self.position[prev_pos]
			self.board[a][b] = 'p.'
			self.board[c][d] = '  '
		else:
			print('Invalid move')
		return cond


