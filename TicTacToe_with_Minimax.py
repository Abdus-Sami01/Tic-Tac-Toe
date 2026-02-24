import math

def create_board():
    board= [[0,1,2],
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
        if board[row][col] != "*" and board[row][col] != "o":
            board[row][col] = "*"
        elif 0 <= move <= 8:
            print("this position is already taken")
        else:
            print("Enter a valid board position between 0-8")




def check_win():
    if ((board[0][0] == "*" and board[0][1] == "*" and board[0][2] == "*")
        or 
        (board[0][0] == "*" and board[1][1] == "*" and board[2][2] == "*")
        or
        (board[0][0] == "*" and board[1][0] == "*" and board[2][0] == "*")
        or 
        (board[1][0] == "*" and board[1][1] == "*" and board[1][2] == "*")
        or
        (board[2][0] == "*" and board[1][1] == "*" and board[0][2] == "*")
        or 
        (board[2][0] == "*" and board[2][1] == "*" and board[2][2] == "*")
        or
        (board[0][1] == "*" and board[1][1] == "*" and board[2][1] == "*")
        or
        (board[0][2] == "*" and board[1][2] == "*" and board[2][2] == "*")):
            return "*"



    elif(board[0][0] == "o" and board[0][1] == "o" and board[0][2] == "o"
        or 
        board[0][0] == "o" and board[1][1] == "o" and board[2][2] == "o"
        or
        board[0][0] == "o" and board[1][0] == "o" and board[2][0] == "o"
        or 
        board[1][0] == "o" and board[1][1] == "o" and board[1][2] == "o"
        or
        board[2][0] == "o" and board[1][1] == "o" and board[0][2] == "o"
        or 
        board[2][0] == "o" and board[2][1] == "o" and board[2][2] == "o"
        or
        board[0][1] == "o" and board[1][1] == "o" and board[2][1] == "o"
        or
        board[0][2] == "o" and board[1][2] == "o" and board[2][2] == "o"):
        return "o"

    else: 
        for row in board:
            for cell in row:
                if cell != "*" and cell != "o":
                    return None
        
        return "draw"
       

player1=Player1

print("you can only use '*' or 'o' for the board marks \n")

def get_empty_cells():
    empty=[]
    for row in board:
        for cell in row:
            if cell !="*" and cell!= "o":
                empty.append(cell)
    return empty

def place(num,mark):
    row=num//3
    cell=num%3
    board[row][cell] = mark

def minimax( is_maximizing):
    result=check_win()

    if result == "*":
        return -1
    
    elif result== "draw":
        return 0
    
    elif result== "o":
        return 1
    
    if is_maximizing:
        best_score = -math.inf
        for cell in get_empty_cells():
            place(cell, "o")
            score =minimax(False)
            place(cell,cell)
            if score > best_score:
                best_score=score
        return best_score
    
    else:
        best_score= math.inf
        for cell in get_empty_cells():
            place(cell, "*")
            score=minimax(True)
            place(cell,cell)
            if score < best_score:
                best_score=score
        return best_score

    

def best_move():
    best_score = -math.inf
    move = None
    for cell in get_empty_cells():
        place(cell, "o")
        score = minimax(False)
        place(cell, cell)
        if score > best_score:
            best_score = score
            move = cell
    place(move, "o")


def main():
    while True:
        player1.move(int(input("Player1: Enter move from 0-8. Your mark is * \n")))
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
    

main()
