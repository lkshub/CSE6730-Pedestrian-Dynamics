
def Density(map,x,y): 
	pass

class Pedestrain(object):
	def __init__(self,ID,x,y,destination,groupSize):
		self.ID = ID
		self.x = x	#coordinate x
		self.y = y	#coordinate y
		self.destination = destination # randomly assigned destinations
		self.groupSize = groupSize	# randomly assigned group size
	def speed(self):
		density = Density(CAMap,self.x,self.y)
		if True:
			pass
		return 
	def exit(self,CA):
		
		print CA

	def walk(self):
		pass

CA = 3
ins = Pedestrain(1,1,1,1,1)
ins.exit(CA)
CA = 4
ins.exit(CA)

CAMap = [[] for i in range(2000)]
for i in range(2000):
	for j in range(2000):
		CAMap[i].append(Cell(i,j,0))