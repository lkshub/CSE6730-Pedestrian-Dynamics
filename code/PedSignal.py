class PedSignal(object):
    state = True
    def __init__(self, x1, y1, x2, y2, greenTime, redTime):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.greenTime = greenTime
        self.redTime = redTime
        self.state = True
        self.change = False

    def signalState(self, t):
        if t%(self.greenTime + self.redTime) <= self.greenTime:
            if not self.state:
                self.change  =True
            self.state = True
            return True
        else:
            if self.state:
                self.change = True
            self.state = False
            return False

    def crossState(self,t,CAMap):
        self.state = self.signalState(t)
        peoOut = []
        if self.change:
            for x in range(self.x1,self.x2+1):
                for y in range(self.y1,self.y2+1):
                    if self.state:
                        CAMap[x][y].UpdateState(0)
                    else:
                        if CAMap[x][y].state>=1:
                            peoOut.append(CAMap[x][y].state)
                        CAMap[x][y].UpdateState(-5)
            self.change = False
        return peoOut



