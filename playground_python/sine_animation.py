import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to generate the standing wave
def generate_standing_wave(x, t):
    amplitude = 1.0
    wavelength = 0.5
    frequency = 1.0
    phase_speed = wavelength * frequency
    return amplitude * np.sin(2 * np.pi * (x - phase_speed * t) / wavelength)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 2)
ax.set_ylim(-1, 1)

# Initialize the line object
line, = ax.plot([], [], lw=2)

# Animation initialization function
def init():
    line.set_data([], [])
    return line,

# Animation update function
def update(frame):
    x = np.linspace(0, 2, 1000)
    y = generate_standing_wave(x, frame / 100)  # Adjust the speed of oscillation by changing the divisor
    line.set_data(x, y)
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, init_func=init, blit=True)

# Display the animation
plt.show()
