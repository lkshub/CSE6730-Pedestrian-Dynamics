from Tkinter import *

def initWin(h,w):
	win = Tk()
	win.geometry('1024x1024')
	win.title("CAModel")
	v = StringVar()
	#v="00:00:00"
	timeFrame = Frame(win)
	buttonFrame = Frame(win)
	mapFrame = Frame(win)
	maps = Canvas(mapFrame,bg='grey',height = h,width=w)
	label = Label(timeFrame,text="Time after end of game:  ",font = ('Helvetica',20),height=2).pack(side=LEFT)
	clock = Label(timeFrame,textvariable=v,font = ('Helvetica',20)).pack(side=RIGHT)

	startButton = Button(buttonFrame,text="Start!",font = ('Helvetica',20),height=2).pack(side=LEFT)
	pauseButton = Button(buttonFrame,text="Pause",font = ('Helvetica',20)).pack(side=LEFT)
	conButton = Button(buttonFrame,text="Continue",font = ('Helvetica',20)).pack(side=LEFT)
	clearButton = Button(buttonFrame,text="Clear All",font = ('Helvetica',20)).pack(side=LEFT)

	timeFrame.pack()
	buttonFrame.pack()

	#maplabel = Label(mapFrame,text="map here").pack()
	
	mapFrame.pack()
	maps.pack()
	return [win,maps,clock,v]

