#Krunal Shah
#Player class for Connect4
#November 22, 2011

from Board import *
from random import randint

class Player():
  """A Connect4 player."""
  def __init__(self, color):
    """Create a player, a distinct color, for the board."""
    self._color = color
    
  def getColor(self):
    """Return the Player's color."""
    return self._color
    
class HumanPlayer(Player):
  """Creates a Human Player to play the game."""
  def drop(self, board, graphics):
    """Input a drop from the user."""   
    legal = False
    while not legal:
      maxval = board.getSize() - 2  #Largest legal y-coordinate to place
      (x,y) = graphics.getMouseRelease() #Get the coordinates from the mouse release
      (x,y) = (x,maxval) #Drop the checker into the largest legal y-coord, using the x from the mouse release
      
      count = 0
      #Drop the checker into the the largest available y-coordinate.
      while board.isOccupied(x,y): 
	(x,y) = (x,maxval-count)  	 
	#While the column is full, get a new click from the user. If the new column is not full, drop the checker to the largest available y-coordinate.
	if board.isOccupied(x,0):
	  (x,y) = graphics.getMouseRelease()
	  (x,y) = (x,maxval-count)
	  continue    
	count += 1
      legal = True
      
    return (x,y)
    
class ComputerPlayer(Player):
  """Creates a Computer Player to play the game."""
  def drop(self, board, graphics):
    """Choose a random column to drop the checker."""    
    legal = False
    while not legal:
      maxval = board.getSize() - 2 
      column = randint(0,maxval)
      (x,y) = (column, maxval) #Drops the checker into the largest y-coordinate, given a random column
      count = 0
      #If the y-coordinate is occupied, drop the checker into the next largest y-coordinate.
      while board.isOccupied(x,y): 
	(x,y) = (column,maxval-count)
	#Get a new column when the column is full
	if board.isOccupied(x,0):
	  column = randint(0,maxval)
	  (x,y) = (column,maxval-count)
	  continue
	count += 1
      legal = True
      
    return (x,y)

if __name__ == '__main__':
	p1 = HumanPlayer('X')
	p2 = ComputerPlayer('Z')
	b = Board()
	#p1.drop(b)
	#print b
	p2.drop(b)
	print b
	p2.drop(b)
	print b
	p2.drop(b)
	print b	
	p2.drop(b)
	print b
	p2.drop(b)
	print b	
	p1.drop(b)
	print b
	p1.drop(b)
	print b	

