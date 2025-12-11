import numpy as np
import matplotlib.pyplot as plt

# Problem definitions

l = 50 #mm  Length
a = 110 #mm^2/s  Thermal diffusivity
t = 4 #s  Time simulation
n = 50 # Nodes

# Initialization
dx = l / n
dt = 0.5*dx**2/a #Stability scheme
t_nodes = int(t/dt)

u = np.zeros(n) + 20 # Plate is initially at 20 C

# Boundary conditions

u[0] = 100
u[-1] = 100

# Visualization 

fig, axis = plt.subplots()

pcm = axis.pcolormesh([u],cmap = plt.cm.jet, vmin = 0, vmax = 100)
plt.colorbar(pcm,ax=axis)
axis.set_ylim([-2,3])

# Simulation

counter = 0

while counter < t :

    w = u.copy()

    for i in range(1, n -1):

        u[i] = dt * a * (w[i-1]-2*w[i]+w[i+1]) / dx ** 2 + w[i]
    
    counter += dt

    print('t: {:.3f} [s], Average temperature: {:.2f} Celcius'.format(counter, np.average(u)))

    #Update the plot

    pcm.set_array([u])
    axis.set_title('Distribution at t: {:.3f} [s]'.format(counter))
    plt.pause(0.01)

plt.show()   
