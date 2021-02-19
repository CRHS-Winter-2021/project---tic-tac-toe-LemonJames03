import sys


done = 0
turn = 0
theBoard = []








def printBoard():
  theboard = ('     |     |     \n  '+ theBoard[7] + '  |  '+ theBoard[8] + '  |  '+ theBoard[9] + '  \n_____|_____|_____\n     |     |     \n  '+ theBoard[4] + '  |  '+ theBoard[5] + '  |  '+ theBoard[6] + '  \n_____|_____|_____\n     |     |     \n  '+ theBoard[1] + '  |  '+ theBoard[2] + '  |  '+ theBoard[3] + '  \n     |     |     \n')
  print(theboard)

#3a. (fun) Determine if player is X or O


 
def play():
  global turn
 
  while done == 0:
    if turn % 2 == 0:
      letter = 'X'
      print("X's Turn")
    else:
      letter = 'O'
      print("O's Turn")
    
    move = input('Where would you like to make your move ')
 
    while move not in ['1','2','3','4','5','6','7','8','9']  or  theBoard[int(move)] != ' ':
      print('Can not do that')
      move = (input('Where would you like to make your move ')
 
      
    theBoard[int(move)] = letter
    
    printBoard()
    win()
    draw()
    turn += 1

def win():
 
 
  
 
  if theBoard[1] == 'X' and theBoard[2] == 'X' and theBoard[3] == 'X'  or  theBoard[4] == 'X' and theBoard[5] == 'X' and theBoard[6] == 'X'  or  theBoard[7] == 'X' and  theBoard[8] == 'X' and theBoard[9] == 'X'  or  theBoard[7] == 'X' and theBoard[4] == 'X' and theBoard[1] == 'X'  or  theBoard[8] == 'X' and theBoard[5] == 'X' and theBoard[2] == 'X'  or  theBoard[9] == 'X' and theBoard[6] == 'X' and theBoard[3] == 'X'  or  theBoard[7] == 'X' and theBoard[5] == 'X' and theBoard[3] == 'X'  or  theBoard[9] == 'X' and theBoard[5] == 'X' and theBoard[1] == 'X':
  
    print('X Wins!')
    sys.exit()
  
  if theBoard[1] == 'O' and theBoard[2] == 'O' and theBoard[3] == 'O'  or  theBoard[4] == 'O' and theBoard[5] == 'O' and theBoard[6] == 'O'  or  theBoard[7] == 'O' and theBoard[8] == 'O' and theBoard[9] == 'O'  or  theBoard[7] == 'O' and theBoard[4] == 'O' and theBoard[1] == 'O'  or  theBoard[8] == 'O' and theBoard[5] == 'O' and theBoard[2] == 'O'  or  theBoard[9] == 'O' and theBoard[6] == 'O' and theBoard[3] == 'o'  or  theBoard[7] == 'O' and theBoard[5] == 'O' and theBoard[3] == 'O'  or  theBoard[9] == 'O' and theBoard[5] == 'O' and theBoard[1] == 'O':
    print('O Wins!')
    sys.exit()

def draw():
  if theBoard.count(' ') == 0:
    done = 1
    print('Draw!')
    sys.exit()



def main():
  global turn
  global theBoard
  print("Welcome to Garrett's Tic Tac Toe Mini Game")
  print("The board is relative to the number pad on your key board")
    
  first = input('Player1 type 1 if you would like to be x and 2 for o ')
  while first != 1 and first != 2:
    input('You need to put 1 or 2.\n Type 1 for x and 2 for o')  
    if first == '2':
      turn += 1
    theBoard = ['blank', '', '', '', '', '', '', '', '', '']

    
main()
printBoard()
play()
