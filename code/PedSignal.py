greenTime = 20
redTime = 40

class PedSignal(object):
    state = True
    def __init__(self, x1, y1, x2, y2, greenTime, redTime):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.greenTime = greenTime
        self.redTime = redTime

    def signalState(self, t):
        if t%(greenTime + redTime) <= greenTime:
            self.state = True
            return True
        else:
            self.state = False
            return False

    def crossState(self):
        for x in xrange(x1,x2):
            for y in xrange(y1,y2):
                if self.state:
                    CAMap[x,y].UpdateState(0)
                else:
                    if CAMap[x,y].state>=1:
                        peoNum = peoNum - 1
                    CAMap[x,y].UpdateState(-1)



