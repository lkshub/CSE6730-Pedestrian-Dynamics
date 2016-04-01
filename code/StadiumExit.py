import Pedestrian
global peoOutside,peoInside,Queue
import RanGenNew as RG
#import random as ra
global totalNum


class StadiumExit(object):
    def __init__(self, x1, y1,x2,y2,index,flow): #Suppose the exit is a line
        self.x1 = x1 #coordinate x1
        self.y1 = y1 #coordinate y1
        self.x2 = x2 #coordinate x2
        self.y2 = y2 #coordinate y2
        self.index = index #index
        self.t = 0 # exit time
        self.RNG=RG.ClassRanGen()
        self.flow = flow


    def egress(self,CAMap,Queue,totalNum,peoInside,dest):
        y=min(self.y1,self.y2)
        x=min(self.x1,self.x2)
        if self.checkClear(CAMap):
            self.t = self.t + 1
            peoOut = self.flow.PdistSetup()
            for i in range(peoOut):
                RN=int(self.RNG.Rand()*12)
                p = Pedestrian.Pedestrian(totalNum-peoInside+i+1,x,y,dest[RN],1)
                p.updateDistance(CAMap)
                if self.x1!=self.x2:
                    x = x + 1
                else:
                    y = y + 1
                Queue.put([p.distance,p])
                #print p.destination
                #print p.distance
            return peoOut
        else:
            return 0

    def checkClear(self,CAMap):
    	check = True
    	x=min(self.x1,self.x2)
    	y=min(self.y1,self.y2)
    	if self.x1 == self.x2:
    	    for j in range(y,self.y1+self.y2-y+1):
                if CAMap[x][j].state !=0 :
                    check = False
                    #break
        else:
            for i in range(x,self.x1+self.x2-x+1):
                if CAMap[i][y].state !=0 :
                    check = False
                    #break
        return check