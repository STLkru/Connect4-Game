#Krunal Shah
#SelectionList method for Connect4
#December 7, 2011

from cs1graphics import *

def selectionList(can,selections,bgcolor='black'):
	"""Display a menu, wait for the user to make a selection, and return
	a number from 0 to len(selections)-1 indicating the user's choice.
	"""
	
	hpad = 20  # padding to left and right of box and also of selections
	vpad = 20  # padding above box and above title
	sgap = 100  # pixel gap between selection boxes

	header = Text('Connect 4')
	(tw,th) = header.getDimensions()
	
	(boxw,boxh) = (550,650)
	box = Rectangle(boxw,boxh,centerPt = Point(0,vpad+boxh/2))
	box.setFillColor('black')
	
	winbox = Layer()
	winbox.add(box)
	winbox.add(header)
	winbox.move(can.getWidth()/2,0)

	itemy = 2*vpad+th/2 + sgap + th
	ycenters = list()
	#Creates a box with appropriate dimenstions, white border, and yellow font for any number of selection
	for item in selections:
		r = Rectangle(boxw-2*hpad,sgap/3+th+25,centerPt = Point(0,itemy))
		r.setFillColor('black')
		r.setBorderColor('white')
		winbox.add(r)
		text = Text(item, fontsize = 20, centerPt = Point(0,itemy))
		text.setFontColor('yellow')
		winbox.add(text)
		ycenters.append(itemy)
		itemy += sgap + th

	can.add(winbox)
	
	#Creates the Connect4 heading at the top
	rectbox = Rectangle(548,100)
	rectbox.setFillColor('black')
	rectbox.setBorderColor('white')	
	
	title = Layer() 
	titletext = Text('C O N N E C T 4', fontsize = 35)
	titletext.setFontColor('green')
	title.add(rectbox)
	title.add(titletext)
	title.moveTo(550/2,650/2-275)
	can.add(title)

	# Wait for a selection
	selected = -1
	while selected == -1:
		e = can.wait()
		if e.getDescription() != 'mouse release':
			continue
		click = e.getMouseLocation()
		# Check x coordinate in range
		clickx = click.getX()
		if clickx < can.getWidth()/2 - boxw/2 + hpad:
			# too far left
			continue
		if clickx > can.getWidth()/2 + boxw/2 - hpad:
			# too far right
			continue
			
		# Base selection off of y coordinate
		clicky = click.getY()
		for i in range(len(ycenters)):
			if abs(clicky - ycenters[i]) < (sgap/3 + th)/2:
				selected = i
	
	# Got a selection, clean up and return it
	can.remove(winbox)
	return selected
		
if __name__ == '__main__':
	
	c = Canvas(550,650)

	print 'Select one'
	names = ['Test1','Test2', 'Test3','Test4']
	selection = selectionList(c,names)
	print 'Item',selection,':',names[selection],'was selected.'

	c.close()