import Cell as CE
import Pedestrian as PE
import StadiumExit
import PedSignal as PS
import MapPrint as MP
import drawWin as DW
import time
import Queue
import Destination
import Pdist as Pd
import DistCal as DC

from Tkinter import *

readfile = open("map3 - Bobby and Tech closed off.csv","r")
w = open("results3.csv","w")

totalNum =50000 #number of people to be evacuated
xLength = 745 #South-North length of the map
yLength = 845 #East-West length of the map
peoInside = totalNum
peoOutside = 0
timeStep = 0
stadiumExitNum = 10
signalNum = 2
r=1
destinationNum = 12

#flow distribution
flow = Pd.ClassPdist(5,15,totalNum)

# Initialize the CA model map
line = readfile.readline()
CAMap = [[] for i in range(xLength)]
for i in range(xLength):
	line = readfile.readline()
	#print line
	stateList = line.split(",")
	for j in range(yLength):
		CAMap[i].append(CE.Cell(i,j,int(stateList[j])))
#draw the map with more details: walking zones, no walking zones, signals(crosswalk), stadium exits
	#Exits of stadiums
stadExits = []
exitLocation = [[609,426,609,440],[591,400,591,414],[344,416,358,416],[212,416,226,416],[153,446,153,460],[103,468,103,482],[103,630,103,644],[110,811,124,811],[444,811,458,811],[689,797,689,811]]
for i in range(stadiumExitNum): 
	e = StadiumExit.StadiumExit(exitLocation[i][0],exitLocation[i][1],exitLocation[i][2],exitLocation[i][3],i+1,flow)
	stadExits.append(e)
	# crosswalk signals
crossSignals = []
signalLocation = [[730,822,739,840],[740,809,740,813]]
for i in range(signalNum): 
	if i==1:
		s = PS.PedSignal(signalLocation[i][0],signalLocation[i][1],signalLocation[i][2],signalLocation[i][3],50,100)
	if i==0:
		s = PS.PedSignal(signalLocation[i][0],signalLocation[i][1],signalLocation[i][2],signalLocation[i][3],100,0)
	crossSignals.append(s)

	#Initialize Distance Map for each destination
DC.DistCal(CAMap,destinationNum,xLength,yLength)

	#Define Destinations
destinations = []
for i in range(destinationNum):
	destinations.append(Destination.Destination(i+1))


#Initialize the GUI
interFace= DW.createWin(r*yLength,r*xLength)
[win,maps,clock,peoInlabel,peoOutlabel,peoExitlabel]  = interFace.link()
#MP.MapPrint(maps,CAMap,r)
MP.MapPrint(maps,CAMap,r,True)
clock.config(text=str(timeStep*0.3)+"s   ")
peoInlabel.config(text = "People Inside: "+str(peoInside))
peoOutlabel.config(text = "  People Outside: "+str(peoOutside))
win.update()

q = Queue.PriorityQueue()

w.write("timeStep,peoInside,peoOutside\n")
#simulation begins!
while peoInside+peoOutside>0:
	timeStep = timeStep + 1 # every time step equals to 0.3 s
	peoOutCross = []
	qtemp = Queue.PriorityQueue()
	
	#generating people from exit
	for i in range(stadiumExitNum):
		if peoInside > 0:
			out = stadExits[i].egress(CAMap,q,totalNum,peoInside,destinations)
			peoInside = peoInside - out
			peoOutside = peoOutside + out

	#signal state check
	for i in range(signalNum):
		peoOutCross.extend(crossSignals[i].crossState(timeStep,CAMap))

	#people movement(walking or exiting the map)
	walkingliveNum = peoOutside
	for i in range(walkingliveNum):
		walkinglive = q.get()
		if walkinglive[1].ID in peoOutCross:
			peoOutside = peoOutside -1
			continue
		currentCell = CAMap[walkinglive[1].x][walkinglive[1].y]
		currentCell.UpdateState(0)
		walkResult = walkinglive[1].walk(CAMap)
		if walkResult[2]:
			qtemp.put((walkinglive[1].distance,walkinglive[1]))
			CAMap[walkResult[0]][walkResult[1]].UpdateState(walkinglive[1].ID)
		else:
			peoOutside = peoOutside - 1
	q=qtemp
	
	for i in CAMap:
		for j in i:
			if j.state>0 or j.score>0:
				j.updateFieldScore()
	
	if timeStep%20==1: # refresh the GUI every 20 timesteps
		MP.MapPrint(maps,CAMap,r,False)
		clock.config(text=str(timeStep*0.3)+"s   ")
		peoInlabel.config(text = "People Inside: "+str(peoInside))
		peoOutlabel.config(text = "  People Outside: "+str(peoOutside))
		peoExitlabel.config(text = "  People Evacuated: "+str(totalNum-peoInside-peoOutside))
		win.update()
	
	w.write(str(timeStep)+','+str(peoInside)+','+str(peoOutside)+"\n")

win.mainloop()

	
