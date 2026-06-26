
def game_jenerator(player1, player2):
    while True:
        try:
            board_size = int(input("Enter the row/column number of the playing field (3, 5, 7): "))
            if board_size not in (3,5,7):
                print("Invalid entry, please try again")
                continue
        except ValueError or TypeError:
            print("Invalid entry, please try again")
            continue
        break

    board = []
    for i in range(board_size):
        board.append([" "]*board_size)
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
            print(f"{i+1} | " + " | ".join(board[i]) + f" | {i+1}") # .join function is used for iteration in items
            print("------------------")
        print("    A   B   C")
    elif len(board) == 5:
        print("\n    A   B   C   D   E")
        for i in range(len(board)):
            print(f"{i+1} | " + " | ".join(board[i]) + f" | {i+1}")
            print("--------------------------")
        print("    A   B   C   D   E")
    elif len(board) == 7:
        print("\n    A   B   C   D   E   F   G")
        for i in range(len(board)):
            print(f"{i+1} | " + " | ".join(board[i]) + f" | {i+1}")
            print("----------------------------------")
        print("    A   B   C   D   E   F   G")  #there are three cases : length being 3 5 or 7. each case has its own table header

def move_player(board, player_name, player1, player2):
    length = len(board)
    while True:    
        move_to = input(f"Player {player_name}, please enter the direction you want to move your own big stone (N, S, E, W, NE, NW, SE, SW): ").upper()
        if len(move_to) > 2 or move_to not in ["N", "S", "E", "W", "NE", "NW", "SE", "SW"]:
            print("Invalid input, please try again")
            continue
        
        try:
            if player_name == player1["name"]: 
                pl_y_coord = player1["position"][0]
                pl_x_coord = player1["position"][1]
            elif player_name == player2["name"]:
                pl_y_coord = player2["position"][0]
                pl_x_coord = player2["position"][1]  # with the if elif case the funciton can work on both players

            movement_dict = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1), "NE": (-1, 1), "NW": (-1, -1), "SE": (1, 1), "SW": (1, -1)}

            move_to = movement_dict.get(move_to)
            y_change = move_to[0]
            x_change = move_to[1]

            board[pl_y_coord][pl_x_coord] = " " # before moving, the previous block is made empty
            pl_y_coord += y_change
            pl_x_coord += x_change
            if pl_y_coord == -1 or pl_x_coord == -1 or board[pl_y_coord][pl_x_coord] != " ": # after updating the index of the player, if the position index is negative player is near to the edge therefore cannot move to desired coordinate
                print("Cannot move to that direction, please try again")
                continue

            board[pl_y_coord][pl_x_coord] = player_name # player now has moved in the board

            if player_name == player1["name"]: 
                player1["position"][0] = pl_y_coord
                player1["position"][1] = pl_x_coord
                break
            elif player_name == player2["name"]:
                player2["position"][0] = pl_y_coord
                player2["position"][1] = pl_x_coord # updating the indexes of the moved player
                break

        except IndexError: # 
            print("Invalid block, please try again")
            continue

    return board, player1, player2

def put_stone(board, player):
    while True:
        stone_dest = input(f"Player {player['name']}, please enter the location where you want to place a small stone (like 1A) : ")
        if len(stone_dest) != 2 or stone_dest[0] not in "1234567" or stone_dest[1] not in "ABCDEFGabcdefg" :
            print("Invalid entry, please try again")
            continue

        x = stone_dest[1].upper()
        y = int(stone_dest[0])-1

        put_dict = {"A" : 0, "B":1, "C":2, "D":3, "E":4, "F":5 , "G":6}
        x = put_dict.get(x)
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
    checklist = []
    players = (player1,player2)

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
                            break
                    except IndexError:
                        continue

        if yeswin:
            player["lose"] = True

    if player1["lose"] == True and player2["lose"] == False:
        print(f"Player {player2['name']} wins!")

    elif player1["lose"] == False and player2["lose"] == True:
        print(f"Player {player1['name']} wins!")

    elif player1["lose"] == True and player2["lose"] == True:
        print("Both players lose/win!")

    return yeswin


def main():

    again = "Y"
    player1 = { "name" : "", "position" : [], "lose" : False}
    player2 = { "name" : "", "position" : [], "lose" : False}   

    while True:
        name1 = input("Enter a capital letter to represent player 1 (except O): ").upper()
        if name1 in "O" or len(name1) != 1:
            print("Invalid name, please try again")
            continue
        break
    while True:
        name2 = input("Enter a capital letter to represent player 2 (except O): ").upper()
        if name1 == name2 or name2 in "O" or len(name2) != 1:
            print("Invalid name, please try again")
            continue
        player1["name"] = name1
        player2["name"] = name2
        break

    while again in "Yy": # the loop that makes the game replayable with the predetermined usernames
        player1["position"] = []
        player1["lose"] = False
        player2["position"] = []
        player2["lose"] = False
        game_board, player1, player2 = game_jenerator(player1, player2)
        show_board(game_board)
        while True: # the main loop to play the game

            game_board, player1, player2 = move_player(game_board, player1["name"], player1, player2)
            show_board(game_board)
            yeswin = wincheck(game_board, player1, player2)
            if yeswin:
                break

            game_board = put_stone(game_board, player1)
            show_board(game_board)
            yeswin = wincheck(game_board, player1, player2)
            if yeswin:
                break

            game_board, player1, player2 = move_player(game_board, player2["name"], player1, player2)
            show_board(game_board)
            yeswin = wincheck(game_board, player1, player2)
            if yeswin:
                break
            
            game_board = put_stone(game_board, player2)
            show_board(game_board)
            yeswin = wincheck(game_board, player1, player2)
            if yeswin:
                break

        again = input("Would you like to play again(Y/N)? : ")

    return

main()