class Cell(object):
    def __init__(self,x,y,s):
        self.state = s
        self.density = 0
        self.x = x
        self.y = y
    def UpdateState(self,NewState):
        self.state = NewState
    def UpdateDensity(self,NewDensity):
        self.density = NewDensity
    def display(self):
        print "This is a try"
        print self.density
        print self.state


