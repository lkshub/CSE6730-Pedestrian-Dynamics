import time
 
# Initial coordinates
x0 = 10.0
y0 = 30.0
 
ball_diameter = 30
 
# Get TKinter ready to go
from Tkinter import *
window = Tk()
canvas = Canvas(window, width=400, height=300, bg='white')
canvas.pack()
 
# Lists which will contain all the x and y coordinates. So far they just
# contain the initial coordinate
x = [x0]
y = [y0]
 
# The velocity, or distance moved per time step
vx = 10.0 # x velocity
vy = 5.0 # y velocity
 
# Boundaries
x_min = 0.0
y_min = 0.0
x_max = 400.0
y_max = 300.0
 
# Generate x and y coordinates for 500 timesteps
for t in range(1, 500):
 
    # New coordinate equals old coordinate plus distance-per-timestep
    new_x = x[t-1] + vx
    new_y = y[t-1] + vy
 
    # If a boundary has been crossed, reverse the direction
    if new_x >= x_max or new_x <= x_min:
        vx = vx*-1.0
 
    if new_y >= y_max or new_y <= y_min:
        vy = vy*-1.0
 
    # Append the new values to the list
    x.append(new_x)
    y.append(new_y)
 
# For each timestep
for t in range(1, 500):
 
    # Create an circle which is in an (invisible) box whose top left corner is at (x[t], y[t])
    canvas.create_oval(x[t], y[t], x[t]+ball_diameter, y[t]+ball_diameter, fill="blue", tag='blueball')
    canvas.update()
 
    # Pause for 0.05 seconds, then delete the image
    time.sleep(0.005)
    canvas.delete('blueball')
 
# I don't know what this does but the script won't run without it.
window.mainloop()