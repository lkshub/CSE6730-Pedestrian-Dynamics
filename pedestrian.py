

class pedestrian(object):
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




