import math

def create_board():
    board = [[0,1,2],
             [3,4,5],
             [6,7,8]]
    return board

global board 
board = create_board()

print(25 * "*", "\n")
print("initial Tic Tac Toe board\n")
print(board, "\n")
print(25 * "*" )

class Player1:
    def __init__(self):
        pass

    def move(move):
        row = move // 3
        col = move % 3
        if 0 <= move <= 8:
            if board[row][col] != "*" and board[row][col] != "o":
                board[row][col] = "*"
            else:
                print("this position is already taken")
        else:
            print("Enter a valid board position between 0-8")


def check_win_state(temp_board):
    b = temp_board
    win_states = [
        [b[0][0], b[0][1], b[0][2]],
        [b[1][0], b[1][1], b[1][2]],
        [b[2][0], b[2][1], b[2][2]],
        [b[0][0], b[1][0], b[2][0]],
        [b[0][1], b[1][1], b[2][1]],
        [b[0][2], b[1][2], b[2][2]],
        [b[0][0], b[1][1], b[2][2]],
        [b[0][2], b[1][1], b[2][0]],
    ]

    for state in win_states:
        if state == ["*", "*", "*"]:
            return "*"
        if state == ["o", "o", "o"]:
            return "o"

    for row in b:
        for cell in row:
            if cell != "*" and cell != "o":
                return None

    return "draw"


def check_win():
    return check_win_state(board)


def get_empty_cells_state(temp_board):
    empty = []
    for row in temp_board:
        for cell in row:
            if cell != "*" and cell != "o":
                empty.append(cell)
    return empty


def place_state(temp_board, num, mark):
    row = num // 3
    col = num % 3
    temp_board[row][col] = mark

def dfs_best_move():
    stack = []
    visited = set()

    stack.append(( [row[:] for row in board], None ))

    while stack:
        current_board, first_move = stack.pop()

        board_tuple = tuple(tuple(row) for row in current_board)

        if board_tuple in visited:
            continue
        visited.add(board_tuple)

        result = check_win_state(current_board)

        if result == "o":
            return first_move

        if result is not None:
            continue

        for cell in get_empty_cells_state(current_board):
            new_board = [row[:] for row in current_board]
            place_state(new_board, cell, "o")

            if first_move is None:
                stack.append((new_board, cell))
            else:
                stack.append((new_board, first_move))

    remaining = get_empty_cells()
    return remaining[0] if remaining else None

def best_move():
    move = dfs_best_move()
    if move is not None:
        row = move // 3
        col = move % 3
        board[row][col] = "o"

def main():
    while True:
        player_input = int(input("Player1: Enter move from 0-8. Your mark is * \n"))
        Player1.move(player_input)

        print(board[0], "\n", board[1], "\n", board[2])

        result = check_win()
        if result == "*":
            print("*"*10, "Victory: Player 1 wins", "*"*10)
            break
        elif result == "draw":
            print("*"*10, "Draw", "*"*10)
            break
        
        best_move()

        print(board[0], "\n", board[1], "\n", board[2])

        result = check_win()
        if result == "o":
            print("*"*10, "Victory: AI wins", "*"*10)
            break
        elif result == "draw":
            print("*"*10, "Draw", "*"*10)
            break
        
        print("Empty cells remaining:\t", get_empty_cells())


def get_empty_cells():
    return get_empty_cells_state(board)


main()