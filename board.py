#!/usr/bin/python
# Author:   @BlankGodd
# chess board

class Board:
	
	def __init__(self):
		self.board = [
			[8,"R.","N.","B.","K.","Q.","B.","N.","R."], #0
			[7,"p.","p.","p.","p.","p.","p.","p.","p."], #1
			[6,"  ","  ","  ","  ","  ","  ","  ","  "], #2
			[5,"  ","  ","  ","  ","  ","  ","  ","  "], #3
			[4,"  ","  ","  ","  ","  ","  ","  ","  "], #4
			[3,"  ","  ","  ","  ","  ","  ","  ","  "], #5
			[2,"p ","p ","p ","p ","p ","p ","p ","p "], #6
			[1,"R ","N ","B ","K ","Q ","B ","N ","R "], #7
			["","a","b","c","d","e","f","g","h"]
			]
 		

	def print_board(self):
		board = self.board
		print('\n  ','-'*49)
		for i in range(len(board)-1):
			for j in board[i]:
				print("",j, "|", end=" ")
			print('\n  ','-'*49)
		print(' ',end="")
		for i in board[-1]:
			print(i, end='     ')
		print()




if __name__ == '__main__':
	c = Board()
	c.print_board()