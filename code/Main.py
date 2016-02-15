import Cell as CE
import Pedestrian as PE
import StadiumExit 
import PedSignal as PS
import MapPrint as MP
import drawWin as DW
import time
from Tkinter import *

totalNum = 20 #number of people to be evacuated
xLength = 12 #South-North length of the map
yLength = 12 #East-West length of the map
peoInside = totalNum
peoOutside = 0
timeStep = 0
exitNum = 1
signalNum = 0
r=50


# Initialize the CA model map
CAMap = [[] for i in range(xLength)]
for i in range(xLength):
	for j in range(yLength):
		CAMap[i].append(CE.Cell(i,j,0))
#print CAMap 
#draw the map with more details: walking zones, no walking zones, signals(crosswalk), stadium exits
	#Exits of stadiums
stadExits = []
exitLocation = [[0,0,0,0],[2,3,4,5],[3,4,5,6],[4,5,6,7],[5,6,7,8]]
for i in range(exitNum): 
	e = StadiumExit.StadiumExit(exitLocation[i][0],exitLocation[i][1],exitLocation[i][2],exitLocation[i][3],i+1,0)
	stadExits.append(e)
	# crosswalk signals
crossSignals = []
signalLocation = [[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7],[5,6,7,8]]
for i in range(signalNum): 
	s = PS.PedSignal(signalLocation[i][0],signalLocation[i][1],signalLocation[i][2],signalLocation[i][3],1,1)
	crossSignals.append(s)
	# non-walking zone
#Initialize the GUI
[win,maps,clock,v] = DW.initWin(r*xLength,r*yLength)

#maps.create_line(0,0,100,100,fill="red")


#
#simulation begins!
while peoInside+peoOutside>0:
	break

	timeStep = timeStep + 1 # every time step means 0.3 s

	#generating people from exit
	for i in range(exitNum):
		if stadExits[i].checkClear(CAMap):
			stadExits[i].time = stadExits[i].time + 1
			stadExits[i].egress()
			'''then randomly distribute people to exits'''

	#signal state check
	

	#people movement(walking)
	pass
	
	#print the map

win.mainloop()
	
	
