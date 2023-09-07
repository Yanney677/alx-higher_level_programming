#!/usr/bin/env python3
import sys

	def is_valid(board, row, col):
	"""
	Check if it's safe to place a queen at a given position on the board.

	Args:
	
	board (list): List representing the chessboard.
	row (int): Row index to check.
	col (int): Column index to check.

	Returns:
	bool: True if it's safe to place a queen, False otherwise.
	"""
	for prev_col in range(col):
	prev_row = board[prev_col]
	if prev_row == row or \
		prev_row - prev_col == row - col or \
		prev_row + prev_col == row + col:
		return False
	return True

	def solve_nqueens(n):
	"""
	Solve the N-Queens puzzle and return all solutions.

	Args:
	n (int): The size of the chessboard and the number of queens to place.

	Returns:
	list: A list of solutions, where each solution is represented as a list
		of column indices for queens placed in each row.
	"""
	def backtrack(col):
	if col == n:
		solutions.append(board[:])  # Found a solution
		return
	for row in range(n):
		if is_valid(board, row, col):
		board[col] = row
		backtrack(col + 1)
		board[col] = -1  # Backtrack

	board = [-1] * n  # Initialize the board with -1 to represent empty squares
	solutions = []
	backtrack(0)  # Start from the first column
	return solutions

	if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: nqueens.py N")
		sys.exit(1)
	if not sys.argv[1].isdigit():
		print("N must be a number")
		sys.exit(1)

	n = int(sys.argv[1])
	if n < 4:
		print("N must be at least 4")
		sys.exit(1)

	solutions = solve_nqueens(n)
	for solution in solutions:
	print(solution)
	print("Found %d solutions" % len(solutions))
