def flowDistr(t):
	totalNum = 50000
	return flow

class StadiumExit(object):
    def __init__(self, x1, y1,x2,y2,i,time): #Suppose the exit is a line
        self.x1 = x1 #coordinate x
        self.y1 = y1 #coordinate y
        self.x2 = x2 #coordinate x
        self.y2 = y2 #coordinate y
        self.i = i #index
        self.t = time
    def egress(self):
    	return flowDistr(self.t)

    def checkClear(self,CAMap):
    	check = True
    	for i in range(self.x1,self.x2+1):
            j = (self.y1-self.y2)/(self.x1-self.x2)*(i-self.x1)+self.y1
            if CAMap[i][j].state !=0 :
                check = False
                break
        return check
