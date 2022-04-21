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

main()
