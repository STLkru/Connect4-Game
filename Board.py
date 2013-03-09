#Krunal Shah
#Board class for Connect4
#November 22, 2011

class Board():
  """A Connect Four board."""
  def __init__(self, size = 6):
    """Create a board with '#'."""
    self._size = size
    self._board = list()
    for row in range(self._size):
      self._board.append(['#']*self._size)
      
  def getSize(self):
    """Return the size of the board."""
    return self._size
    
  def setSquare(self,x,y,color):
    """Store the colored checker at position (x,y)."""
    self._board[x][y] = color
    
  def getSquare(self,x,y):
    """Get the coordinates of the colored checker."""
    return self._board[x][y]
    
  def isOccupied(self,x,y):
    """Return True if position (x,y) is free."""
    return self._board[x][y] != '#'
    
  def wouldMoveWin(self,x,y,value):
    """Tests for wins by placing value at (x,y)."""
    win = False

    # Temporarily make the move
    self._board[x][y] = value
		
    #Check for horizontal win 
    for x in range(self._size): #Check every column
      for y in range(self._size): #Check every row
	if self._board[x][y] == value and self._board[x+1][y] == value and self._board[x+2][y] == value and self._board[x+3][y] == value: 
	  win = True
    
    #Check for vertical win 
    for x in range(self._size): 
      for y in range(self._size): 
	if self._board[x][y] == value and self._board[x][y+1] == value and self._board[x][y+2] == value and self._board[x][y+3] == value:
	  win = True    
    
    #Check for SE diagnol '\' win 
    for x in range(self._size):
      for y in range(self._size):
	if self._board[x][y] == value and self._board[x+1][y+1] == value and self._board[x+2][y+2] == value and self._board[x+3][y+3] == value:
	  win = True
    
    #Check for NE diagnol '/' win
    for x in range(self._size):
      for y in range(self._size): 
	if self._board[x][y] == value and self._board[x+1][y-1] == value and self._board[x+2][y-2] == value and self._board[x+3][y-3] == value:
	  win = True 
	
    # Un-make the move:
    self._board[x][y] = '#'	
    return win
    
  def __str__(self):
    """Convert to a printable, multi-line string."""
    out = ''
    for y in range(self._size):
      for x in range(self._size-1):#Draw one less column, because inputting the largest column, in the Player Class, raises an error
	out += self.getSquare(x,y)
      out += '\n'
    return out
    
if __name__ == '__main__':
  b = Board()
  print 'empty board, size', b.getSize()  
  b.setSquare(0,5,'X')
  b.setSquare(0,4,'X')
  b.setSquare(0,3,'X')
  b.setSquare(4,5,'0')
  #if b.wouldMoveWin(0,2,'X'):
    #print 'winner'
  print b
  if b.isOccupied(0,3):
    print 'true'
  if b.isOccupied(1,5):
    print 'true'
  else:
    print 'false'
    
  b.getSquare(4,5)
