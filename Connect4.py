#Krunal Shah
#Connect4 game
#November 22, 2011

from Board import *
from Player import *
from GraphicsManager import*

class Connect4():
  """A Connect4 game."""
  def __init__(self, size = 9):
    """Connect 4 game for a given size board."""
    try:
      Menu() #Display the menu as soon as the program is run
      gman = GraphicsManager(size)
    
      playertypenames = ['Player vs. Player','Player vs Computer', 'Computer vs Player','Computer vs. Computer'] #Different combinations of games to play in Connect4
      playertypes = [HumanPlayer,ComputerPlayer] #Different types of players 
    
      wantstoplay = True
      while wantstoplay:
      
	gametype = gman.selectFromList(playertypenames) 
	#Depending on the user click, choose the type of game to play.
	if gametype == 0:
	  players = [playertypes[gametype]('Red'),playertypes[gametype]('Blue')] #Player1 vs. Player2
	if gametype == 1:
	  players = [playertypes[gametype-1]('Red'),playertypes[gametype]('Blue')] #Player vs. Computer (Player goes first)
	if gametype == 2:
	  players = [playertypes[gametype-1]('Red'),playertypes[gametype-2]('Blue')] #Computer vs. Plyer (Computer goes first)
	if gametype == 3:
	  players = [playertypes[gametype-2]('Red'),playertypes[gametype-2]('Blue')] #Computer vs. Computer
      
	#Game Play
	board = Board(size)
	movesleft = (size-1)*(size-1) #Number of moves until board is full
      
	gameOver = False
	while not gameOver:
	  #Alternates turns among two players 
	  for p in players: 
	    (x,y) = p.drop(board,gman) #Get the player's move
	    winner = board.wouldMoveWin(x,y,p.getColor()) #Test for win  
	    board.setSquare(x,y,p.getColor()) #Play the move
	    movesleft -= 1 #Subtract 1 every time a player makes a move
	    gman.displayMove(x,y,p.getColor()) 
	    
	    #Exit the loop if either player has won, or if it is a draw
	    if winner or movesleft == 0: 
	      gameOver = True
	      break 
	  
	#Report the result of the game
	if winner:
	  result = 'W I N N E R !'
	  gman.displayResult(result, p.getColor())
     
	else:
	  result = "D R A W"
	  gman.displayResult(result, 'green')
    
    except AttributeError:
      print 'Congratulations to the Winner!'
    
	  
if __name__ == '__main__':
  Connect4()
	
