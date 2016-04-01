
import Queue

import findDistance as fD

from Tkinter import *

def DistCal(CAMap,destinationNum,xLength,yLength):

	exitNear = [[] for i in range(destinationNum)]
	for i in range(26):
		exitNear[0].append( [4+i,5])
	for i in range(25):
		exitNear[1].append( [5,4+i])
	for i in range(20):
		exitNear[2].append( [5,397+i])
	for i in range(30):
		exitNear[3].append( [5,594+i])
	for i in range(25):
		exitNear[4].append( [5,816+i])
	for i in range(25):
		exitNear[5].append( [4+i,839])
	for i in range(14):
		exitNear[6].append( [729+i,839])
	for i in range(7):
		exitNear[7].append( [739,808+i])
	for i in range(8):
		exitNear[8].append( [739,398+i])
	for i in range(7):
		exitNear[9].append( [734+i,5])
	for i in range(21):
		exitNear[10].append( [441+i,5])
	for i in range(20):
		exitNear[11].append( [247+i,839])
	#print exitNear
	for destinationID in range(destinationNum):
		q = Queue.Queue()
		for cell in exitNear[destinationID]: 
			x = cell[0]
			y = cell[1]
			CAMap[x][y].DistToExit[destinationID] = 1

		for cell in exitNear[destinationID]: 
			x = cell[0]
			y = cell[1]
			for i  in range(-1,2):
				for j in range(-1,2):
					if x+i <1 or x+i>xLength-2 or y+j <1 or y+j >yLength-2:
						continue
					if (CAMap[x+i][y+j].DistToExit[destinationID] == 0)and(CAMap[x+i][y+j].state == 0):
						q.put([x+i,y+j])

		while not q.empty():
			newCell = q.get()
			x = newCell[0]
			y = newCell[1]
			if fD.findDistance(destinationID,x,y,CAMap):
				for i  in range(-1,2):
					for j in range(-1,2):
						if x+i <1 or x+i>xLength-2 or y+j <1 or y+j >yLength-2:
							continue
						if (CAMap[x+i][y+j].DistToExit[destinationID] == 0)and(CAMap[x+i][y+j].state == 0):
							q.put([x+i,y+j])





