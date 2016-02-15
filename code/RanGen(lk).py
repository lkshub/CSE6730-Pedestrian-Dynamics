class RanGen(object):

    def __init__(self,seed):
        self.seed=seed
        self.a=13
        self.c=0
        self.m=31
    def Rand(self):
        self.seed=(self.a*int(self.seed)+self.c)%self.m
        RanNo=round(float(self.seed)/float(self.m),5)
        print("updatedSeed",self.seed)
        print("Rand_Number",RanNo)
        return RanNo


r= RanGen(5)
r.Rand()
r.Rand()
r.Rand()