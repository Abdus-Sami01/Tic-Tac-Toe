["*" for _ in range(25)]

board= [[0,1,2],
        [3,4,5],
        [6,7,8]]

print(25 * "*", "\n")
print("initial Tic Tac Toe board\n")
print(board, "\n")
print(25 * "*" )



class Player1:
    def __init__(self):
        pass

    def move(move):
        if move==1:
            if not (board[0][0]=="o"):
                board[0][0] = "*"
            else:
                print("this position is already taken")

        elif move==2:
            if not (board[0][1]=="o"):
              board[0][1] = "*"
            else:
                print("this position is already taken")

        elif move==3:
            if not (board[0][2]=="o"):
                board[0][2] = "*"
            else:
                print("this position is already taken")

        elif move==4:
            if not (board[1][0]=="o"):
             board[1][0] = "*"
            else:
                print("this position is already taken")


        elif move==5:
            if not (board[1][1]=="o"):
             board[1][1] = "*"
            else:
                print("this position is already taken")


        elif move==6:
            if not (board[1][2]=="o"):
               board[1][2] = "*"
            else:
                print("this position is already taken")


        elif move==7:
            if not (board[2][0]=="o"):
                board[2][0] = "*"
            else:
                print("this position is already taken")


        elif move== 8:
            if not (board[2][1]=="o"):
              board[2][1] = "*"
            else:
                print("this position is already taken")


        elif move == 9:
            if not (board[2][2]=="o"):
             board[2][2] = "*"
            else:
                print("this position is already taken")

        else:
            print("Enter a valid board position")



class Player2:
    def __init__(self):
        pass

    def move(move):
        if move==1:
            if not (board[0][0]=="*"):
               board[0][0] = "o"
            else:
                print("this position is already taken")

        elif move==2:
            if not (board[0][1]=="*"):
               board[0][1] = "o"
            else:
                print("this position is already taken")

        elif move==3:
            if not (board[0][2]=="*"):
              board[0][2] = "o"
            else:
                print("this position is already taken")

        elif move==4:
            if not (board[1][0]=="*"):
             board[1][0] = "o"
            else:
                print("this position is already taken")

        elif move==5:
            if not (board[1][1]=="*"):
              board[1][1] = "o"
            else:
                print("this position is already taken")

        elif move==6:
            if not (board[1][2]=="*"):
              board[1][2] = "o"
            else:
                print("this position is already taken")

        elif move==7:
            if not (board[2][0]=="*"):
               board[2][0] = "o"
            else:
                print("this position is already taken")

        elif move== 8:
            if not (board[2][1]=="*"):
                board[2][1] = "o"
            else:
                print("this position is already taken")

        elif move == 9:
            if not (board[2][2]=="*"):
               board[2][2] = "o"
            else:
                print("this position is already taken")

        else:
            print("Enter a valid board position")

def check_win():
    print(board[0],"\n",board[1],"\n",board[2])
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
            print("*"*10, "Victory: Player 1 wins", "*"*10)
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
        print("*"*10, "Victory: Player 2 wins", "*"*10) 
        return "o"

    else: 
        for row in board:
            for cell in row:
                if cell != "*" and cell != "o":
                    return None
        
        print("*" * 10, "Draw", "*"*10)
        return "Draw"
       

player1=Player1
player2=Player2

print("you can only use '*' or 'o' for the board marks \n")

def get_empty_cells():
    empty=[]
    for row in board:
        for cell in row:
            if cell !="*" and cell!= "o":
                empty.append(cell)
    return empty


while True:
    for i in range(3):
     player1.move(int(input("Player1: Enter move from 1-9. Your mark is * \n")))
     player2.move(int(input("Player2: Enter move from 1-9. Your mark is o \n")))
     print("Current Board", board)
     print("Empty cells remaining:\t",get_empty_cells())
    check_win()

    if check_win():
        break

    else:
        continue


