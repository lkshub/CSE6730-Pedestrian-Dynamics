from Tkinter import *

class createWin:
	def __init__(self,w,h):
		self.win = Tk()
		self.win.geometry('1200x1024')
		self.win.title("CAModel")
		self.h = h
		self.w = w
		timeFrame = Frame(self.win)
		#buttonFrame = Frame(self.win)
		mapFrame = Frame(self.win)
		self.maps = Canvas(mapFrame,height = self.h,width=self.w,bg="grey")
		self.time = Label(timeFrame,text="Time after end of game:  ",font = ('Helvetica',20),height=2).pack(side=TOP)
		self.clock = Label(timeFrame,text="0",font = ('Helvetica',20))
		self.clock.pack(side=TOP)
		self.peoInlabel =Label(timeFrame,text="0",font = ('Helvetica',20))
		self.peoInlabel.pack(side=TOP)
		self.peoOutlabel =Label(timeFrame,text="0",font = ('Helvetica',20))
		self.peoOutlabel.pack(side=TOP)
		self.peoExitlabel =Label(timeFrame,text="0",font = ('Helvetica',20))
		self.peoExitlabel.pack(side=TOP)
		#startButton = Button(buttonFrame,text="Start!",font = ('Helvetica',20),height=2,command=self.start()).pack(side=LEFT)
		#pauseButton = Button(buttonFrame,text="Pause",font = ('Helvetica',20),command=self.pause()).pack(side=LEFT)
		#conButton = Button(buttonFrame,text="Continue",font = ('Helvetica',20)).pack(side=LEFT)
		#clearButton = Button(buttonFrame,text="Clear All",font = ('Helvetica',20)).pack(side=LEFT)

		timeFrame.pack(side=LEFT)
		#buttonFrame.pack()
		self.isStart = False
		self.isPause = False
		#maplabel = Label(mapFrame,text="map here").pack()
		
		mapFrame.pack(side=LEFT)
		self.maps.pack()
		
	def link(self):
		return [self.win,self.maps,self.clock,self.peoInlabel,self.peoOutlabel,self.peoExitlabel]
	def start(self):
		self.isStart = True
	def pause(self):
		self.isPause = True
#def isStart():
