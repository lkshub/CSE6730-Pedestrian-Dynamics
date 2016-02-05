#import Cell.Cell
#import pedestrian.pedestrian
xLength = 10000 #South-North length of the map
yLength = 10000 #East-West length of the map

def Density(map,x,y): 
	pass

c = Cell(1,1,0)
# Initialize the CA model map
CAMap = [[] for i in range(xLength)]
for i in range(xLength):
	for j in range(yLength):
		CAMap[i].append(Cell(i,j,0))

CA = 3
ins = pedestrian(1,1,1,1,1)
ins.exit(CA)
CA = 4
ins.exit(CA)

FirstCell = Cell(1,1,1)
FirstCell.display()
FirstCell.UpdateDensity(1)
FirstCell.UpdateState(1)
FirstCell.display()