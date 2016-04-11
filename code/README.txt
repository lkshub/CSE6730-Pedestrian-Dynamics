------
README for the Program
------

--	This software is written with Python 2.7. Testing environments includes MAC OSX 10.11.3 and Windows10.
	Some additional libraries should be installed for running this program:
		numpy, datetime, matplot

--	The main entrance of the software is the Main.py, which has three versions: Main1.py, Main2.py and Main3.py, respectively corresponding to three different scenarios:
	—All roads stay open, i.e. pedestrian only use side walk. 	—All roads closed off for pedestrian to evacuate. 	—Bobby Dodd Way NW closed off for pedestrian to evacuate.

—	map1.csv, map2 - all roads closed off.csv, map3 - Bobby and Tech closed off.csv are three map data files, respectively corresponding to the three different scenarios

--	Main.py would then in return call other classes or functions: Pedestrain.py, Cell.py, StadiumExit.py, PedSignal.py, MapPrint.py, drawWin.py, Pdist.py and DistCal.py,Destination.py.
	—Pedestrain.py includes the definition of class Pedestrian, which has attributes and functions including: id, coordinates, speed, destination, groupsize, destination,preference matrix and walk
	—Cell.py includes the definition of class Cell which has attributes and functions include: State, score, updateState, updateScore.
	—StadiumExit.py includes the definition of class StadiumExit, which has attributes and functions including: coordinates, egress and checkClear
	—PedSignal.py includes the definition of class PedSignal, which has attributes and functions include: coordinates, greenTime/redTime period, crossState.
	—MapPrint.py includes the function MapPrint for print the simulation results to GUI
	—drawWin.py includes the definition of  class drawWin for the creation of GUI
	—Pdist.py includes the definition of  class Pdist for the flow distribution generator
	—DistCal.py includes the function DistCal for calculating the static field score with Dynamic Programming
	—Destination.py includes the definition of class Destination with attributes: id, coordinates

--	The modules not directly utilized by main.py are:
	—RanGenNew.py, which generates random numbers for StadiumExit and Pedestrians
	—findDistance.py, which is used by DistCal for calculating the minimum distance
