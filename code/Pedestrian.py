#import random
import RanGenNew as RG
import DistCal

def density(CAMap,x,y): 
	states = []
	sum = 0
	for i in range(5):
		for j in range(5):
			states.append(CAMap[x-2+i][y-2+j].state)

	for w in range(25):
		if not states[w] == 0:
			sum = sum+1

	return (sum / 25)

class Pedestrian(object):
	def __init__(self,ID,x,y,destination,groupSize):
		self.ID = ID
		self.x = x	#coordinate x
		self.y = y	#coordinate y
		self.destination = destination # randomly assigned destinations
		self.groupSize = groupSize	# randomly assigned group size
		self.distance = 0
		self.RNG = RG.ClassRanGen()
	def getSpeed(self,CAMap):
		den = density(CAMap,self.x,self.y)
		if den <0.5:
			return 2
		else:
			return 1

	def walk(self,CAMap):
		self.distance = self.updateDistance(CAMap)
		if CAMap[self.x][self.y].DistToExit[self.destination.id-1]==1:
			return [self.x, self.y, False]
		fI = self.findIndex(self.prefMat(CAMap),CAMap)
		self.x = self.x + fI[0] - 2
		self.y = self.y + fI[1] - 2
		self.distance = self.updateDistance(CAMap)
		return [self.x, self.y, True]


	def updateDistance(self,CAMap):
		return CAMap[self.x][self.y].DistToExit[self.destination.id-1]
	def prefMat(self,CAMap):
		sc = [0.75, 0.75, 0.5,0.25,0.15]
		prefM = [ [0 for x in range(5)] for y in range(5) ]
		for j in range (5):
			for i in range(5):
				if CAMap[self.x-2+i][self.y-2+j].state != 0:
					prefM[i][j] = 0
				else:
					dist = (CAMap[self.x-2+i][self.y-2+j].DistToExit[self.destination.id-1])
					if self.distance <= dist:
						RN2 = self.RNG.Rand()
						prefM[i][j] = RN2
					else:
						RN1 = self.RNG.Rand()+1
						prefM[i][j] = ((CAMap[self.x-2+i][self.y-2+j].score) + (self.distance-dist))*RN1
					
					if (i==2 and j==2):
						RN2 = self.RNG.Rand()
						prefM[i][j] = RN2*0.8

		return prefM

	def findIndex(self, matrix,CAMap):
		bigX = 2
		bigY = 2
		scoretemp = 0
		if self.getSpeed(CAMap) == 2:
			for j in range(5):
				for i in range(5):
					if matrix[i][j]>scoretemp:
						bigX = i
						bigY = j
						scoretemp = matrix[i][j]
		else:
			for j in range(3):
				for i in range(3):
					if matrix[i+1][j+1]>scoretemp:
						bigX = i+1
						bigY = j+1
						scoretemp = matrix[i+1][j+1]
		return [bigX, bigY]


