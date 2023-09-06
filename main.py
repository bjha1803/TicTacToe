# boxes on board table
boxes={1:' ',2:' ',3:' ',
        4:' ',5:' ',6:' ',
        7:' ',8:' ',9:' '}
# board table
def BoardTable():
    print()
    print(f"{boxes[1]} | {boxes[2]} | {boxes[3]}")
    print("----------")
    print(f"{boxes[4]} | {boxes[5]} | {boxes[6]}")
    print("----------")
    print(f"{boxes[7]} | {boxes[8]} | {boxes[9]}")
    print()

# checking if someone's win
def IsWin():
    if boxes[1]==boxes[2]==boxes[3]!=' ':
        return True
    if boxes[4]==boxes[5]==boxes[6]!=' ':
        return True
    if boxes[7]==boxes[8]==boxes[9]!=' ':
        return True
    if boxes[1]==boxes[4]==boxes[7]!=' ':
        return True
    if boxes[2]==boxes[5]==boxes[8]!=' ':
        return True
    if boxes[3]==boxes[6]==boxes[9]!=' ':
        return True
    if boxes[1]==boxes[5]==boxes[9]!=' ':
        return True
    if boxes[3]==boxes[5]==boxes[7]!=' ':
        return True
    
# checking if Draws
def IsDraw():
    for i in range(1,10):
        if(boxes[i])==' ':
            return False
    return True

# Player1's turn
def Player1():
    turn=int(input("Player1 Enter Your Choice(1-9): "))
    if(turn<1 or turn>9):
        print("Number should be between 1 to 9")
        print("Please play again")
        Player1()
    else:
        if(boxes[turn]==' '):
            boxes[turn]='X'
        else:
            print("Invalid Choice. please enter again")
            Player1()

# Player2's turn
def Player2():
    turn=int(input("Player2 Enter Your Choice(1-9): "))
    if(turn<1 or turn>9):
        print("Number should be between 1 to 9")
        print("Please play again")
        Player2()
    else:
        if(boxes[turn]==' '):
            boxes[turn]='O'
        else:
            print("Invalid Choice. please enter again")
            Player2()

while True:
    BoardTable()
    Player1()
    BoardTable()
    if IsWin():
        BoardTable()
        print("Player 1 is the winner")
        break
    if IsDraw():
        print("Draw")
        break
    Player2()
    if IsWin():
        BoardTable()
        print("Player 2 is the winner")
        break
    if IsDraw():
        print("Draw")
        break
    
    



