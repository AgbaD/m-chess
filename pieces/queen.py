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

	def white_take(self, ab, player):
		cond = self.check_north(ab,player)
		if not cond:
			self.check_east(ab,player)
		if not cond:
			self.check_west(ab,player)
		if not cond:
			self.check_south(ab,player)
		if cond:
			a,b = self.position[ab]
			c,d = self.position[cond]
			self.board[a][b] = "Q "
			self.board[c][b] = "  "
			print("Q{}x{}".format(cond,ab))
			return True
		return cond

	def black_take(self, ab, player):
		cond = self.check_north(ab,player)
		if not cond:
			self.check_east(ab,player)
		if not cond:
			self.check_west(ab,player)
		if not cond:
			self.check_south(ab,player)
		if cond:
			a,b = self.position[ab]
			c,d = self.position[cond]
			self.board[a][b] = "Q."
			self.board[c][b] = "  "
			print("Q.{}x{}".format(cond,ab))
			return True
		return cond	
	
	def move_white(self, ab, player):
		cond = self.check_north(ab,player)
		if not cond:
			self.check_east(ab,player)
		if not cond:
			self.check_west(ab,player)
		if not cond:
			self.check_south(ab,player)
		if cond:
			a,b = self.position[ab]
			c,d = self.position[cond]
			self.board[a][b] = "Q "
			self.board[c][b] = "  "
			return True
		print(cond)
		return cond

	def move_black(self, ab, player):
		cond = self.check_north(ab,player)
		if not cond:
			self.check_east(ab,player)
		if not cond:
			self.check_west(ab,player)
		if not cond:
			self.check_south(ab,player)
		if cond:
			a,b = self.position[ab]
			c,d = self.position[cond]
			self.board[a][b] = "Q."
			self.board[c][b] = "  "
			return True
		return cond

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
			j = int(num) + i
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
			for i in range(1,8):
				j = int(num) + i
				if j > 8:
					break
				k = self.alpha[alp]
				k += i
				if k > 8:
					break
				k = self.alpha[k]
				pos = k+str(j)
				a,b = self.position[pos]
				if self.board[a][b] != "  ":
					if self.board[a][b] == check:
						prev_pos = pos
						cond = True
						break
					else:
						break
		if not cond:
			# north west
			for i in range(1,8):
				j = int(num) + i
				if j > 8:
					break
				k = self.alpha[alp]
				k -= i
				if k < 1:
					break
				k = self.alpha[k]
				pos = k+str(j)
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

	def check_east(self,ab,player):
		check = ""
		prev_pos = ""
		if player == 1:
			check = 'Q '
		else:
			check = "Q."
		cond = False
		# qe3
		alp,num = ab[0],ab[-1]
		for i in range(1, 8):
			j = self.alpha[alp]
			j += i
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

	def check_west(self,ab,player):
		check = ""
		prev_pos = ""
		if player == 1:
			check = 'Q '
		else:
			check = "Q."
		cond = False
		# qe3
		alp,num = ab[0],ab[-1]
		for i in range(1, 8):
			j = self.alpha[alp]
			j -= i
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
		if cond:
			return prev_pos
		return cond

	def check_south(self,ab,player):
		check = ""
		prev_pos = ""
		if player == 1:
			check = "Q "
		else:
			check = "Q."
		cond = False
		# vertical south
		# qe3
		alp,num = ab[0],ab[-1]
		for i in range(1,8):
			j = int(num) - i
			if  j > 1:
				break
			pos = alp + str(j)
			a,b = self.position[pos]
			if self.board[a][b] != "  ":
				if self.board == check:
					prev_pos = pos
					cond = True
					break
				else:
					break
		if not cond:
			# south east
			for i in range(1,8):
				j = int(num) - i
				if j < 1:
					break
				k = self.alpha[alp]
				k += i
				if k > 8:
					break
				k = self.alpha[k]
				pos = k + str(j)
				a,b = self.position[pos]
				if self.board[a][b] != "  ":
					if self.board[a][b] == check:
						prev_pos = pos
						cond = True
						break
					else:
						break
		if not cond:
			# south west
			for i in range(1,8):
				j = int(num) - i
				if j < 1:
					break
				k = self.alpha[alp]
				k -= i
				if k < 1:
					break
				k = self.alpha[k]
				pos = k + str(j)
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

