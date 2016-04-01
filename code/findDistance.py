def findDistance(exitID,x,y,CAMap):
	#print[x,y]
	if CAMap[x][y].DistToExit[exitID] != 0:
		return False
	
	temp = 2147483647
	for i  in [-1,0,1]:
		for j in [-1,0,1]:
			#print [x+i,y+j,CAMap[x+i][y+j].DistToExit[exitID-1]]
			if (CAMap[x+i][y+j].state < 0)or(CAMap[x+i][y+j].DistToExit[exitID] == 0):
				continue
			#print [x,y,x+i,y+j,CAMap[x+i][y+j].DistToExit[exitID-1]]
			if CAMap[x+i][y+j].DistToExit[exitID]+1 < temp:
				temp = CAMap[x+i][y+j].DistToExit[exitID]+1
				#print 100
	CAMap[x][y].DistToExit[exitID]= temp

	#print CAMap[x][y].DistToExit[exitID]
	return True