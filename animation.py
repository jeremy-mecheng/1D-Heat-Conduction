import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

## Problem definitions
l = 50  # mm  Length
a = 110  # mm^2/s  Thermal diffusivity
t_sim_end = 4  # s Time simulation (Renombrado para evitar conflicto con 't' de tiempo actual)
n = 100  # Nodes

# Initialization
dx = l / n
dt = 0.5 * dx**2 / a  # Stability scheme

# Plate is initially at 20 C
u = np.zeros(n) + 20

# Boundary conditions
u[0] = 100
u[-1] = 100

## Initial visualization configuration
fig, axis = plt.subplots(figsize=(8, 4)) 
axis.set_ylim([-2, 3])
axis.set_xlabel("Nodes (Position)")
axis.set_yticks([]) 
#axis.set_title("Heat conduction in 1D")

# Create the initial color
pcm_init = axis.pcolormesh([u], cmap=plt.cm.jet, vmin=0, vmax=100)
cbar = plt.colorbar(pcm_init, ax=axis, orientation='horizontal', pad=0.2)
cbar.set_label('Temperature (°C)')
pcm_init.remove() 


# Simulation

ims = []  
current_time = 0
step_count = 0
save_interval = 25 

while current_time < t_sim_end:
    w = u.copy()
    for i in range(1, n - 1):
        u[i] = dt * a * (w[i-1] - 2*w[i] + w[i+1]) / dx**2 + w[i]
    
    current_time += dt
    step_count += 1

    if step_count % save_interval == 0:
        pcm = axis.pcolormesh([u], cmap=plt.cm.jet, vmin=0, vmax=100, animated=True)
        time_text = axis.text(0.5, 1.05, f'Tiempo: {current_time:.3f} [s]', 
                              ha='center', transform=axis.transAxes, animated=True, fontsize=12)
    
        ims.append([pcm, time_text])
        
        if step_count % (save_interval*10) == 0:
             print(f"Simulando t: {current_time:.3f} s")

ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)

output_filename = '1D-Heat-Diffusion.gif'
ani.save(output_filename, writer='pillow', fps=20)
plt.close() # Cierra la figura al terminar para liberar memoria