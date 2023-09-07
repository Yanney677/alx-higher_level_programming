#!/usr/bin/python3

"""N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

N must be an integer greater than or equal to 4.

Attributes:
    board (list): list of lists representing the chessboard.
    solutions (list): list of lists containing solutions
"""
import sys


def init_board(n):
    """initialize an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for j in range(m)]
    [row.append(' ') for j in range(m) for row in board]
    return (board)


def board_deepcopy(board):
    """return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """return the list of lists representation of a solved chessboard."""
    solution = []
    for s in range(len(board)):
        for a in range(len(board)):
            if board[s][a] == "Q":
                solution.append([s, a])
                break
    return (solution)


def xout(board, row, col):
    """X out spots on a chessboard.

    Args:
        board (list): current working chessboard.
        row (int): row where a queen was last played.
        col (int): column where a queen was last played.
    """
    # X out all forward spots
    for a in range(col + 1, len(board)):
        board[row][a] = "x"
    # X out all backwards spots
    for a in range(col - 1, -1, -1):
        board[row][a] = "x"
    # X out all spots below
    for s in range(row + 1, len(board)):
        board[s][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        board[s][col] = "x"
    # X out all spots diagonally down to the right
    a = col + 1
    for s in range(row + 1, len(board)):
        if a >= len(board):
            break
        board[s][a] = "x"
        c += 1
    # X out all spots diagonally up to the left
    a = col - 1
    for s in range(row - 1, -1, -1):
        if a < 0:
            break
        board[s][a]
        a -= 1
    # X out all spots diagonally up to the right
    a = col + 1
    for s in range(row - 1, -1, -1):
        if a >= len(board):
            break
        board[s][a] = "x"
        a += 1
    # X out all spots diagonally down to the left
    a = col - 1
    for s in range(row + 1, len(board)):
        if a < 0:
            break
        board[s][a] = "x"
        a -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens.

    Args:
        board (list): current working chessboard.
        row (int): current working row.
        queens (int): current number of placed queens.
        solutions (list): list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for a in range(len(board)):
        if board[row][a] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][a] = "Q"
            xout(tmp_board, row, a)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
    print("Found %d solutions" % len(solutions))

    sys.exit(0)
