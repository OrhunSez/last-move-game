
def empty_generator(board_size):
    board = []
    for i in range(board_size):
        board.append([" "]*board_size)
    return board

def game_jenerator(board, player1, player2):
    board_size=len(board)
    insert_player_index = int(board_size/2)
    board[0][insert_player_index] = player2["name"]
    board[board_size-1][insert_player_index] = player1["name"] #player 1 and player 2 are put to the beginning positions
    player1["position"] = [board_size-1, insert_player_index]
    player2["position"] = [0, insert_player_index] # a list is used to store the beginning index data of the players
    return board, player1, player2

def show_board(board):
    if len(board) == 3:
        print("\n    A   B   C")
        for i in range(len(board)):
            print(f"{i + 1} | " + " | ".join(board[i]) + f" | {i + 1}") # .join function is used for iteration in items
            print("------------------")
        print("    A   B   C")
    elif len(board) == 5:
        print("\n    A   B   C   D   E")
        for i in range(len(board)):
            print(f"{i + 1} | " + " | ".join(board[i]) + f" | {i + 1}")
            print("--------------------------")
        print("    A   B   C   D   E")
    elif len(board) == 7:
        print("\n    A   B   C   D   E   F   G")
        for i in range(len(board)):
            print(f"{i + 1} | " + " | ".join(board[i]) + f" | {i + 1}")
            print("----------------------------------")
        print("    A   B   C   D   E   F   G")  #there are three cases : length being 3 5 or 7. each case has its own table header

def move_player(board, player_name, player1, player2):
    length = len(board)
    while True:    
        move_to = input(f"Player {player_name}, please enter the direction you want to move your own big stone (N, S, E, W, NE, NW, SE, SW): ").upper()
        try:
            if player_name == player1["name"]: 
                a = player1["position"][0]
                b = player1["position"][1]
            elif player_name == player2["name"]:
                a = player2["position"][0]
                b = player2["position"][1]  # with the if elif case the funciton can work on both players

            if move_to == "N" and a > 0:
                if board[a-1][b] == " ":
                    board[a][b] = " "
                    board[a-1][b] = player_name
                    a-=1
                else:
                    print("Occupied block, try again")
                    continue
            elif move_to == "S" and a < length:
                if board[a+1][b] == " ":
                    board[a][b] = " "
                    board[a+1][b] = player_name
                    a+=1
                else:
                    print("Occupied block, try again")
                    continue
            elif move_to == "E" and b < length:
                if board[a][b+1] == " ":
                    board[a][b] = " "
                    board[a][b+1] = player_name
                    b+=1
                else:
                    print("Occupied block, try again")
                    continue
            elif move_to == "W" and b > 0:
                if board[a][b-1] == " ":
                    board[a][b] = " "
                    board[a][b-1] = player_name
                    b-=1
                else:
                    print("Occupied block, try again")
                    continue
            elif move_to == "NE" and a > 0 and b < length:
                if board[a-1][b+1] == " ":
                    board[a][b] = " "
                    board[a-1][b+1] = player_name
                    a-=1
                    b+=1
                else:
                    print("Occupied block, try again")
                    continue
            elif move_to == "NW" and a > 0 and b > 0 :
                if board[a-1][b-1] == " ":
                    board[a][b] = " "
                    board[a-1][b-1] = player_name
                    a-=1
                    b-=1
                else:
                    print("Occupied block, try again")
                    continue
            elif move_to == "SE" and a < length and b < length:
                if board[a+1][b+1] == " ":
                    board[a][b] = " "
                    board[a+1][b+1] = player_name
                    a+=1
                    b+=1
                else:
                    print("Occupied block, try again")
                    continue
            elif move_to == "SW" and a < length and b > 0:    
                if board[a+1][b-1] == " ":
                    board[a][b] = " "
                    board[a+1][b-1] = player_name
                    a+=1
                    b-=1
                else:
                    print("Occupied block, try again")
                    continue

            else:
                print("No such direction, try again.")
                continue

            if player_name == player1["name"]: 
                player1["position"][0] = a
                player1["position"][1] = b
                break
            elif player_name == player2["name"]:
                player2["position"][0] = a
                player2["position"][1] = b # updating the indexes of the moved player
                break

        except IndexError:
            print("Invalid block, please try again")
            continue

    return board, player1, player2

def put_stone(board, player):
    while True:
        stone_dest = input(f"Player {player['name']}, please enter the location where you want to place a small stone (like 1A) : ")
        if stone_dest[0] not in "1234567" or stone_dest[1] not in "ABCDEFGabcdefg" or len(stone_dest) != 2:
            print("Invalid entry, please try again")
            continue

        x = stone_dest[1].upper()
        y = int(stone_dest[0])-1

        match x:
            case "A":
                x = 0
            case "B":
                x = 1
            case "C":
                x = 2
            case "D":
                x = 3
            case "E":
                x = 4
            case "F":
                x = 5
            case "G":
                x = 6 
        try:
            if board[y][x] == " ":
                board[y][x] = "O"
                break
            else:
                print("Occupied block, try again")
                continue
        except IndexError:
            print("Invalid block, please try again")
            continue

    return board

def wincheck(board, player1, player2):
    global checklist
    checklist = []

    players = [player1,player2]

    for player in players:
        x = player["position"][0]
        y = player["position"][1]
        yeswin = True

        if x>0 and y >0:
            for i in range(-1,2):
                for j in range(-1,2):
                    try:
                        checklist.append(board[x+i][y+j])
                        if board[x+i][y+j] == " ":
                            yeswin = False # there is no winning state if an empty block exists around the player
                            print("nowin")
                            break
                    except IndexError:
                        continue

        elif x==0 and y >0:
            for i in range(2):
                for j in range(-1,2):
                    try:
                        checklist.append(board[x+i][y+j])
                        if board[x+i][y+j] == " ":
                            yeswin = False 
                            print("nowin")
                            break
                    except IndexError:
                        continue
        
        elif x>0 and y==0:
            for i in range(-1,2):
                for j in range(2):
                    try:
                        checklist.append(board[x+i][y+j])
                        if board[x+i][y+j] == " ":
                            yeswin = False 
                            print("nowin")
                            break
                    except IndexError:
                        continue

        else:
            for i in range(2):
                for j in range(2):
                    try:
                        checklist.append(board[x+i][y+j])
                        if board[x+i][y+j] == " ":
                            yeswin = False 
                            print("nowin")
                            break
                    except IndexError:
                        continue

        if yeswin:
            player["lose"] = True

    if player1["lose"] == True and player2["lose"] == False:
        print(f"Player {player2['name']} wins!")

    if player1["lose"] == False and player2["lose"] == True:
        print(f"Player {player1['name']} wins!")

    if player1["lose"] == True and player2["lose"] == True:
        print("Both players lose/win!")

    return yeswin


def main():

    again = "Y"

    while again in "Yy":
        player1 = { "name" : "", "position" : [], "lose" : False}
        player2 = { "name" : "", "position" : [], "lose" : False}   
        player1name = input("Enter a capital letter to represent player 1 (except O): ").upper()
        player2name = input("Enter a capital letter to represent player 2 (except O): ").upper()
        player1["name"] = player1name
        player2["name"] = player2name
        board_size = int(input("Enter the row/column number of the playing field (3, 5, 7): "))
        game_board = empty_generator(board_size)
        game_board, player1, player2 = game_jenerator(game_board, player1, player2)
        show_board(game_board)
        while True:
            game_board, player1, player2 = move_player(game_board, player1["name"], player1, player2)
            show_board(game_board)
            game_board = put_stone(game_board, player1)
            show_board(game_board)
            yeswin = wincheck(game_board, player1, player2)
            if yeswin:
                break
            game_board, player1, player2 = move_player(game_board, player2["name"], player1, player2)
            show_board(game_board)
            game_board = put_stone(game_board, player2)
            show_board(game_board)
            yeswin = wincheck(game_board, player1, player2)
            if yeswin:
                break

        again = input("Would you like to play again(Y/N)? : ")

    return

main()