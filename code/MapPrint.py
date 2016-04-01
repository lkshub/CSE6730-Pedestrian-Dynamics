
from Tkinter import *

def MapPrint(maps,CAMaps,r,isInit):
	for i in CAMaps:
		for j in i:
			s = j.state
			x = j.y
			y = j.x
			if isInit or j.isChange:
				j.isChange = False
				if not isInit and s < 0:
					continue
				elif s > 0:
					maps.create_rectangle(x*r+1,y*r+1,(x+1)*r,(y+1)*r,fill="black")
					#maps.create_text(x*r+1+r/2,y*r+1+r/2, text = str(s),fill = "white")
				elif s == 0:
					maps.create_rectangle(x*r+1,y*r+1,(x+1)*r,(y+1)*r,fill="PaleGreen",outline="PaleGreen")
				elif s == -9:
					maps.create_rectangle(x*r+1,y*r+1,(x+1)*r,(y+1)*r,fill="purple",outline="purple")
				elif s in [-2,-3,-4]:
					maps.create_rectangle(x*r+1,y*r+1,(x+1)*r,(y+1)*r,fill="yellow",outline="yellow")
				elif s == -5:
					maps.create_rectangle(x*r+1,y*r+1,(x+1)*r,(y+1)*r,fill="red",outline="red")
