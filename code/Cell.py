class Cell(object):
    def __init__(self,x,y,s):
        self.state = s
        #self.conjection = 0 #do not need density here
        self.x = x
        self.y = y
        self.score = 0
        self.DistToExit=[0 ,0, 0, 0, 0, 0,0,0,0,0,0,0]
        self.isChange = False

    def UpdateState(self,NewState):
        self.state = NewState
        self.isChange  =True
    #def UpdateConjection(self):
        #self.conjection = self.conjection*0.9 + 1
    def updateFieldScore(self):
        self.score = self.score * 0.5 + (self.state > 0) 
'''
    def displ(self):
        print "This is a try"
        print self.density
        print self.state
'''
