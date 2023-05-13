import random

def testWin(grid, i, j, playerType):
  grid1 = copyGrid(grid)
  if grid1[i][j] != ' ':
    return False
  
  grid1[i][j] = playerType
  
  return checkWin(grid1, playerType)

def testFork(grid, playerType):
  if playerType == 'O':
    op = 'X'
    
  if playerType == 'X':
    op = 'O'

  grid1 = copyGrid(grid)
  if grid1[1][1] == op or grid1[1][1] == "":
    return False
    
  corners = cornerCheck(grid1, playerType)
  for i in corners:
    if i == [0, 0] and grid1[0][2] == ' ':
      grid1[0][2] = 'O'
      return grid1
    if i == [0, 0] and grid1[2][0] == ' ':
     grid1[2][0] = 'O'
     return grid1
    
    if i == [0, 2] and grid1[0][0] == ' ':
      grid1[0][0] = 'O'
      return grid1
    if i == [0, 2] and grid1[2][2] == ' ':
      grid1[2][2] = 'O'
      return grid1
    
    if i == [2, 0] and grid1[0][0] == ' ':
      grid1[0][0] = 'O'
      return grid1
    if i == [2, 0] and grid1[2][2] == ' ':
      grid1[2][2] = 'O'
      return grid1
    
    if i == [2, 2] and grid1[0][2] == ' ':
      grid1[0][2] = 'O'
      return grid1
    if i == [2, 2] and grid1[2][0] == ' ':
      grid1[2][0] = 'O'
      return grid1
  return False

def testFork(grid, i, j, playerType):
  grid1 = copyGrid(grid)
  if grid1[i][j] != ' ':
    return False
    
  grid1[i][j] = playerType
  
  wins = 0
  for i in range(3):
    for j in range(3):
      if grid1[i][j] == ' ':
        grid1[i][j] = 'O'
        if checkWin(grid1, playerType):
          wins += 1
        grid1[i][j] = ' '
        
  if wins > 1:
    return True
  
def cornerCheck(grid, playerType):
  corners = []
  if grid[0][0] == playerType:
    corners.append([0, 0])
  if grid[0][2] == playerType:
    corners.append([0, 2])
  if grid[2][0] == playerType:
    corners.append([2, 0])
  if grid[2][2] == playerType:
    corners.append([2, 2])
  return corners

def copyGrid(grid):
  newGrid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
  for i in range(3):
    for j in range(3):
      newGrid[i][j] = grid[i][j]
  return newGrid

def AISelect2(grid):
  
  #check winning moves
  for i in range(3):
    for j in range(3):
      if testWin(grid, i, j, 'O'):
        grid[i][j] = 'O'
        return grid
  #check defensive moves     
  for i in range(3):
    for j in range(3):
      if testWin(grid, i, j, 'X'): 
        grid[i][j] = 'O'
        return grid
        
  for i in range(3):
    for j in range(3):
      if testFork(grid, i, j, 'O'): 
        print("fork")
        grid[i][j] = 'O'
        return grid

  for i in range(3):
    for j in range(3):
      if testFork(grid, i, j, 'X'): 
        print("fork1")
        grid[i][j] = 'O'
        return grid
        
  
  #check center
  if grid[1][1] == ' ':
    grid[1][1] = 'O'
    return grid 
    
  #check corners
  if grid[0][0] == ' ':
    grid[0][0] = 'O'
    return grid 
    
  if grid[0][2] == ' ':
    grid[0][2] = 'O'
    return grid 
    
  if grid[2][0] == ' ':
    grid[2][0] = 'O'
    return grid 
    
  if grid[2][2] == ' ':
    grid[2][2] = 'O'
    return grid 
    
  #check sides
  if grid[0][1] == ' ':
    grid[0][1] = 'O'
    return grid
    
  if grid[1][0] == ' ':
    grid[1][0] = 'O'
    return grid
  
  if grid[1][2] == ' ':
    grid[1][2] = 'O'
    return grid
  
  if grid[2][1] == ' ':
    grid[2][1] = 'O'
    return grid
    
  
        
def checkTie(grid):
  count = 0
  for i in range(3):
    for j in range(3):
      if grid[i][j] != ' ':
        count+=1
  if count == 9:
    return True
  return False
  
#this is where I check my grid
def checkWin(grid, playerType):
  if grid[0][0] == playerType and grid[0][1] == playerType and grid[0][2] == playerType:
    return True
    
  if grid[1][0] == playerType and grid[1][1] == playerType and grid[1][2] == playerType:
    return True
    
  if grid[2][0] == playerType and grid[2][1] == playerType and grid[2][2] == playerType:
    return True
    
  if grid[0][0] == playerType and grid[1][0] == playerType and grid[2][0] == playerType:
    return True
    
  if grid[0][1] == playerType and grid[1][1] == playerType and grid[2][1] == playerType:
    return True
    
  if grid[0][2] == playerType and grid[1][2] == playerType and grid[2][2] == playerType:
    return True
    
  if grid[0][0] == playerType and grid[1][1] == playerType and grid[2][2] == playerType:
    return True
    
  if grid[2][0] == playerType and grid[1][1] == playerType and grid[0][2] == playerType:
    return True
    
  return False
    
#finish if statements later

def printGrid(grid):
  for i in range(3):
    for j in range(3):
      if j != 2:
        print(" "+grid[i][j]+" |",end = "" )
      else:
        print(" "+grid[i][j]+" ")
    if i != 2:
      print("---+---+---")
      

def coinFlip():
  return random.randint(0,1)
  
grid=[[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

print("Hello, welcome to Tic Tac Toe. You are now Player X. A coin flip will decide who goes first, you or Player O(computer).")
flip = coinFlip()
player = ""

if flip == 0:
  print("Player O goes first!")
  player = 'O'
  
else:
  print("Player X goes first!")
  player = 'X'
  
printGrid(grid)
  
while True:
  
  if player == 'X':
    print('Player X Turn:')
    row = input("Please enter the row of the box you would like to play:")
    column = input("Please enter the column of the box you would like to play:")
    grid[int(row)-1][int(column)-1] = 'X'
    printGrid(grid)
    if checkWin(grid, 'X') == True:
      print("Player X won!!! :)")
      break
    player = 'O'
  else:
    print('Player O Turn:')
    grid = AISelect2(grid)
    printGrid(grid)
    if checkWin(grid, 'O') == True:
      print("Player O won. :(")
      break
    player = 'X'
    
  if checkTie(grid):
    print("TIE")
    break

    


