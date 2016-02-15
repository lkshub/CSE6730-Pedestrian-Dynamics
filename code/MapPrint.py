
from Tkinter import *

def MapPrint(maps,x,y,r):
	maps.create_rectangle((x-1)*r+1,(y-1)*r+1,x*r,y*r)