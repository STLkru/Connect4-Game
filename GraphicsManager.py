#Krunal Shah
#Manages graphics for Connect4
#November 30, 2011

from cs1graphics import *
from SelectionList import*

class Menu:
	"""Instructions menu for Connect4."""
	def __init__(self):
		"""Creates a Graphical Instruction menu."""
		self._width = 550
		self._height = 650
		graphic = Canvas(self._width, self._height, 'black',title = 'Connect4')
		
		#Draw the heading, with black background, white border, and green text
		rectbox = Rectangle(550,100)
		rectbox.setFillColor('black')
		rectbox.setBorderColor('white')	
		title = Layer() 
		titletext = Text('C O N N E C T 4', fontsize = 35)
		titletext.setFontColor('green')
		title.add(rectbox)
		title.add(titletext)
		title.moveTo(self._width/2,self._height/2-275)
		graphic.add(title)
		
		#Creates a circle nd puts it on the canvas, right on the 4
		checker = Circle(25, Point(403,50)) 
		checker.setBorderColor('green')
		graphic.add(checker)
		
		#Create an instructions box
		instrbox = Rectangle(250,326)
		instrbox.setBorderColor('white')
		
		instrlayer = Layer() #Create a layer that includes all text graphics in the instructions box
		
		#The following blocks of code create a text graphic, move the position of the graphic, set the font color, and add the text to the instrlayer
		instr = Text('Instructions:', fontsize = 25)
		instr.moveTo(-48,-145)
		instr.setFontColor('white')
		instrlayer.add(instrbox)
		instrlayer.add(instr)
		
		one = Text('1. If playing Player vs. Player,', fontsize = 16)
		one.moveTo(-5,-110)
		one.setFontColor('white')
		one2 = Text('choose who plays first', fontsize = 16)
		one2.moveTo(-17,-92)
		one2.setFontColor('white')
		instrlayer.add(one)
		instrlayer.add(one2)
		
		two = Text('2. To drop, drag the checker', fontsize = 16)
		two.moveTo(-12,-48)
		two.setFontColor('white')
		two2 = Text('or click the column', fontsize = 16)
		two2.moveTo(-30,-30)
		two2.setFontColor('white')
		instrlayer.add(two)
		instrlayer.add(two2)
		
		three = Text('3. Alternate turns among users,', fontsize = 16)
		three.moveTo(0,14)
		three.setFontColor('white')
		three2 = Text('until winner is declared', fontsize = 16)
		three2.moveTo(-12,32)
		three2.setFontColor('white')
		instrlayer.add(three)
		instrlayer.add(three2)
		
		four = Text('4. First player to get 4', fontsize = 16)
		four.moveTo(-35,76)
		four.setFontColor('white')
		four2 = Text('in a row wins', fontsize = 16)
		four2.moveTo(-48,94)
		four2.setFontColor('white')	
		instrlayer.add(four)
		instrlayer.add(four2)
		
		figure = Text('(See Figure on the right)', fontsize = 10) 
		figure.moveTo(0,128)
		figure.setFontColor('white')		
		instrlayer.add(figure)		
		
		instrlayer.moveTo(self._width/2-137.5,self._height/2) #Moves the instrlayer to line up with the .gif image
		graphic.add(instrlayer) #Adds the layer to the Canvas
		
		proceed = Text('(Click Anywhere or Press any Key, to Continue to the Game)', fontsize = 18)
		proceed.setFontColor('green')
		proceed.moveTo(self._width/2,self._height-100)
		graphic.add(proceed)
		
		#Insert a .gif image to the canvas
		win = Image('win.gif')
		win.moveTo(self._width/2+140,self._height/2)
		graphic.add(win)
		
		graphic.wait() #Wait for the user to interact with the canvas
		graphic.close()
	
class GraphicsManager:
	"""Graphics I/O for Connect4."""
	def __init__(self, size = 9):
		"""Create a graphical display of the board."""
		self._size = size
		self._width = 550
		self._squareside = self._width/float(self._size-1) # size of each individual square
		self._canvas = Canvas(self._width,self._width+100,title="Connect4") #Create a canvas with particular dimensions and title
		self._canvas.setBackgroundColor('black')
		
		# Draw the grid
		s = 0
		for i in range(self._size - 1): #Subtract 1, because the last column tends to give an error
			s += self._squareside
			#Draws horizonal lines down the canvas 
			horizontallines = Path(Point(s,0+100),Point(s,self._width+100))
			horizontallines.setBorderColor('white') #White line
			self._canvas.add(horizontallines)
			#Draws vertical lines across the canvas
			verticallines = Path(Point(0,s+100),Point(self._width,s+100)) 
			verticallines.setBorderColor('white')
			self._canvas.add(verticallines)
		topline = Path(Point(0,self._squareside+30),Point(self._width,self._squareside+30)) #Create a new line for the top of the grid
		topline.setBorderColor('white')
		self._canvas.add(topline)
	
	def displayResult(self,result, color):
		"""Display the Winner of the game."""
		winbox = Layer()
		msg = Text(result, fontsize = 50)
		msg.setFontColor(color) #Sets the font color to the color of the winner of the game
		(tw,th) = msg.getDimensions()
		box = Rectangle(tw+200,th) #Sets the rectangle according to the length of the text
		box.setFillColor('black')
		winbox.add(box)
		winbox.add(msg)
		winbox.moveTo(self._width/2,self._width/2-225) #Moves the result to the top, centered
		self._canvas.add(winbox)
		#Wait for a mouse click, then close
		e = self._canvas.wait()
		while e.getDescription() != 'mouse click':
			e = self._canvas.wait()
		self._canvas.close()
	
	def displayMove(self,x,y,color):
		"""Display the checker on the board at the corresponding position."""
		px = (x-0.95) * self._squareside + 100 #Centers the x position of the circle on the grid
		py = (y+0.5) * self._squareside + 100 #Centers the y position of the circle on the grid
		checker = Circle(30,Point(px,py)) #Creates a circle and centers it in the grid
		checker.setFillColor(color)
		checker.setBorderColor('white')
		self._canvas.add(checker)
		
	def getMouseRelease(self):
		"""Return (x,y) board coordinates of a where the mouse is released."""
		
		checker = Circle(25, Point(403,50)) #Creates a circle, that can be dragged, and puts it on the grid right above the 4
		checker.setBorderColor('green')
		self._canvas.add(checker)
		
		e = self._canvas.wait()
		while e.getDescription() != 'mouse release': #Wait for a mouse release, this could be a drag or a firm click
			movingPoint = e.getMouseLocation() 
			checker.moveTo(movingPoint.getX(),50) #Move the x location of the checker, per the mouse
			e = self._canvas.wait()		
		
		p = e.getMouseLocation()
		x = int(p.getX()/self._squareside) #Turns the x coordinate, from the user click, into an integer
		y = int(p.getY()/self._squareside) #Turns the y coordinate, from the user click, into an integer
		self._canvas.remove(checker)

		return (x,y)
		
	def selectFromList(self,selections):
		"""Returns the number of the selected button from what the user selects."""
		return selectionList(self._canvas,selections)

if __name__ == '__main__':
	a = Menu()
	g = GraphicsManager()	
	
	names = ['Test1','Test2','Test3']
	selection = g.selectFromList(names)
	print names[selection],'was selected'
	
	g.displayMove(0,7,'Green')
	g.displayMove(1,7,'Red')
	g.displayMove(0,6,'Yellow')
	g.displayMove(0,5,'Blue')
	g.displayMove(2,7,'Orange')

	for x in range(5):
		print g.getClickedSquare()

	g.displayResult('winner', 'white')
	