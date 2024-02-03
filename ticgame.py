import os
import time 
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 1
Win = 1
draw = -1
run = 0
stop = 1
Game = run
choice = 'X'

def DrawBoard():
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print(" | | ")
def position(x):
    if board [x] == ' '  :
        return True
    else :
        return False
def Winner() :
    global Game
    
    if board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
        Game = Win
    elif board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
        Game = Win
    elif board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
        Game = Win
    elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        Game = Win
    elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        Game = Win
    elif board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
        Game = Win
    elif board[1] == board[5] and board[5] == board[9] and board[5] != ' ':
        Game = Win
    elif board[3] == board[5] and board[5] == board[7] and board[5] != ' ':
        Game = Win
    elif board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and \
            board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and \
            board[7] != ' ' and board[8] != ' ' and board[9] != ' ':
        Game = draw
    else:
        Game = run
print("\t\t\t Welcome\t\t\t ")
print ("\t\t THis game is written by Jdidi Tasnim \t\t")
print("\t\t Player 1 :X  ;  Player 2: Y \t\t ")
print("\t\t\t Loading \t\t\t ")
time.sleep(2)
while Game ==run:
    os.system('cls')
    DrawBoard()
    if player %2 ==0 :
        print("player two choice")
        choice ='O'
    else:
        print("player one choice ")
        choice ='X'
    msg=(int(input("Enter position between [1-9]")))
    if 1 <= msg <= 9 :
        if  position(msg):
            board[msg]= choice
            player +=1
            Winner()
        else:
            print("Position already occupied. Try again.")
            time.sleep(1)
    else:
        print("Invalid input. Position should be between 1 and 9.")
        time.sleep(1)
    os.system('cls')
    DrawBoard()
    if Game ==draw:
        print("Game Draw !!!")
    elif Game ==Win:
        player-=1
        if player %2==0:
            print("player 2 in the winner")
        else:
            print("Player one is the Winner")
            