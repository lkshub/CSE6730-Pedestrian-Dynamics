import os
class ClassRanGen(object):

    def __init__(self,seed):
        self.x=seed
        self.a=13
        self.c=0
        self.m=31
    def Rand(self):
#implement the Random number generater below
        if os.path.isfile('storage.txt'):
            pass
        else:
            file_object=open('storage.txt','w')
            file_object.write('%d\n'%self.x)
            file_object.close()
#
        file_object=open('storage.txt')
        try:
            self.x=file_object.read()
        finally:
            file_object.close()

        self.x=(self.a*int(self.x)+self.c)%self.m
        RanNo=round(float(self.x)/float(self.m),5)
        file_object=open('storage.txt','w')
        file_object.write('%d\n'%self.x)
        file_object.close()
        pass
        print("update_x",self.x)
        print("Rand_Number",RanNo)
        return RanNo
