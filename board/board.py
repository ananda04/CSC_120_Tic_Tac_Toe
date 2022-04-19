board = [['_','_','_'],['_','_','_'],['_','_','_']]
def print_board():
  for item in board:
    print(item)

def check_mark(row, col):
  if row < 0 or row > 2:
    print('incorrect entry. Please give a nuumber from 0 to 2')
    return(False)
  if col< 0 or col>2:
    print('incorrect entry. Please give a nuumber from 0 to 2')
    return(False)
  if board[row][col] == '_':
    return(True)
  return(False)

def place_mark(row, col, player):
  if check_mark(row, col) == True:
    if player == 1:
      board[row][col] = 'X'
    elif player == 2:
      board[row][col] = 'O'
  else:
    print("already occupied")

def check_win(player):
  if player == 1:
    mark = 'X'
  elif player == 2:
    mark = 'O'
  # checking rows
  for i in range(3):
    win = True
    for j in range(3):
      if board[i][j] != mark:
        win = False
        break
    if win:
      return win

  # checking columns
  for i in range(3):
    win = True
    for j in range(3):
        if board[j][i] != mark:
            win = False
            break
    if win:
      return win

  #checking diagonals
  win = True
  for i in range(3):
    if board[i][i] != mark:
        win = False
        break
  if win:
    return win

  win = True
  for i in range(3):
    if board[i][2 - i] != mark:
        win = False
        break
  if win:
    return win
  return False

def main():
  print('testing print_board')
  print_board()
  print('------------')

  check_mark(1,2)
  for i in range(100):
    x = int(input("Please enter x poistion:"))
    y = int(input(" y position and player number:"))
    pid = int(input(" player number [1,2]:"))
    print('------------')

    place_mark(x,y,pid)
    print('------Results------')
    print_board()
    print('------------')
    if check_win(1) == True:
      print("Player 1 has won")
      break
    if check_win(2) == True:
      print("Player 2 has won")
      break
    # if no empty slots then it is a draw
    draw = True
    for row in board:
      for cell in row:
        if cell == '_':
          draw = False
          break
    if draw == True:
      print('Draw')
      break
        

main()

