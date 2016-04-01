# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math as mt
import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt
class ClassPdist(object):
    def __init__(self,u,c,Nt):
        # u is a constant to construct the Poission Distribution （the mean peak time of flux）
        # N is the number of RV of poission dist
        self.N=1
        self.Nt=0
        self.flux=0
        self.Nout=0
        self.Ntotal=Nt
        self.u=u
        self.c=c
# Nout is number of out from stadium
    def PdistSetup(self):
        #this function called only once.
#typically, NtTotal can be 500.
#        u=500000*(2/1)
# set u to fit peak popultion rate below the capacity of exit such 25 people
        

        pp=np.random.poisson(self.u, self.N)
        self.flux=min(pp,self.c)
        self.Nout=self.Nout+self.flux

        if (self.Nout>self.Ntotal):
            self.flux=self.flux-(self.Nout-self.Ntotal)
            #print("ALL PEOPLE HAVE LEAF THE STADIUM!")
    #        print("pp=",pp)
        #print("flux=",max(self.flux))
#        print("max=",max(self.flux))
#if floor(t/45):
    
##        print("bins=",bins)
##        print("flux=",self.flux)
# #       print("sum-flux=",sum(self.flux))
        return self.flux
'''    
    def PdistOutput(self):
#this function needs called each time when allow people appear at the gate of the stadium.
#Nt is not the real time, but the time count for egress    
        self.Nt=self.Nt+1
        if ((self.Nt<=self.NtTotal)and(self.Nout<self.N)):
            flux_output=mt.ceil(self.flux[self.Nt-1])            
            self.Nout=self.Nout+flux_output
            if (self.Nout>self.N):
                self.Nout=self.Nout-flux_output
                flux_output=self.N-self.Nout
            else:
                pass
#            print("the number of out from stadium=",self.Nout)
#            print("flux at this step=",flux_output)
        else:
            flux_output=0
            if (self.Nt>=self.NtTotal-10):
#                print("ALL PEOPLE HAVE LEAF THE STADIUM!")
            else:
                pass
        return flux_output
#    bin_max=bins[-1]
#    bin_min=bins[0]
#10*t+bin_min
#    dt=(bin_max-bin_min)/10
#    t_bin=t+bin_min
#    for i in range(0,60):
#        if (t_bin>bins[i] and t_bin<bins[i+1]):
#            t_index=i
#        else:
#            pass

#t
#print(bin_max-bin_min)
#we need standarize the range of bins

#    plt.show()
'''

#plt.plot([1,2,3,4])
#plt.ylabel('some numbers')
#plt.show()