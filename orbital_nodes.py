import math as m
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import axes3d

import graph
import rotate as rot
import objects as obj

# Create the constant orbit
orbit = obj.generate_ellipse_centered(a=1, e=0, resolution=360)
orbit = rot.rotate_3d(orbit, 0, 0, 90); orbit = rot.rotate_3d(orbit, 25, 0, 0)

# Function to render the full graph
def render_graph(ax, v):
    global orbit

    # If the planet is in the ascending/descending node, draw an arrow to the node
    if 88 <= v <= 92 or 268 <= v <= 272:
        ax.plot([orbit[0][270], orbit[0][90]], [orbit[1][270], orbit[1][90]],
            [orbit[2][270], orbit[2][90]], color='red') 
        obj.draw_arrow_node(ax=ax, v=v)
    else: # Drawing the line of intersection
        ax.plot([orbit[0][270], orbit[0][90]], [orbit[1][270], orbit[1][90]],
            [orbit[2][270], orbit[2][90]], color='black')
        ax.plot([-2, 2], [0, 0], [0, 0], linestyle='dotted', color='black')

    # Drawing the planet's axis
    planet_a = [m.cos(m.radians(v)), m.sin(m.radians(v)), 0]
    planet_a = rot.rotate_3d(planet_a, 0, 0, 90); planet_a = rot.rotate_3d(planet_a, 25, 0, 0)
    ax.plot([planet_a[0], planet_a[0]], [planet_a[1], planet_a[1]], [planet_a[2]-1, planet_a[2]+1], color='grey')
     
    # Drawing the orbit's major axis
    ax.plot([orbit[0][0], orbit[0][180]], [orbit[1][0], orbit[1][180]],
        [orbit[2][0], orbit[2][180]], linestyle='dotted', color='grey')

    # Drawing the planes of reference
    obj.draw_plane(ax, 2, 2, rot_x=25, rot_z=0, colour='blue')
    obj.draw_plane(ax, 2, 2, rot_x=0, rot_z=0, colour='green')

    obj.draw_planet_and_sun(ax=ax, bahn=orbit, v=v)
    ax.plot(orbit[0], orbit[1], orbit[2], color='tab:blue')


# Create the constant orbit for preview
last_angle = 0; resolution = 16; t = np.arange(0, resolution + 1) 
prev_orbit = np.array([np.cos(np.radians(360 / resolution * t)),np.sin(np.radians(360 / resolution * t)),[0] * (resolution + 1)])
prev_orbit = rot.rotate_3d(prev_orbit, 0, 0, 90); prev_orbit = rot.rotate_3d(prev_orbit, 25, 0, 0)

# Function to preview the graph
def preview_graph(ax, v):
    global prev_orbit
    global resolution
    global last_angle

    # Only draw the graph if the angle has changed by at least 10°, or if the planet is in a node, or it has moved away from a node
    if not (88 <= v <= 92 or 268 <= v <= 272):
        if abs(v - last_angle) < 10 and not (88 <= last_angle <= 92 or 268 <= last_angle <= 272):
            return
    last_angle = v
    graph.reset_graph(ax=ax)

    # If the planet is in the ascending/descending node, draw an arrow to the node
    if 88 <= v <= 92 or 268 <= v <= 272:
        ax.plot([prev_orbit[0][3*int(resolution/4)], prev_orbit[0][int(resolution/4)]], [prev_orbit[1][3*int(resolution/4)],
            prev_orbit[1][int(resolution/4)]], [prev_orbit[2][3*int(resolution/4)], prev_orbit[2][int(resolution/4)]], color='red') 
        obj.draw_arrow_node(ax=ax, v=v)
    else: # Drawing the line of intersection
        ax.plot([prev_orbit[0][3*int(resolution/4)], prev_orbit[0][int(resolution/4)]], [prev_orbit[1][3*int(resolution/4)],
            prev_orbit[1][int(resolution/4)]], [prev_orbit[2][3*int(resolution/4)], prev_orbit[2][int(resolution/4)]], color='grey')

    # Drawing the planets axis
    planet_a = [m.cos(m.radians(v)), m.sin(m.radians(v)), 0]
    planet_a = rot.rotate_3d(planet_a, 0, 0, 90); planet_a = rot.rotate_3d(planet_a, 25, 0, 0)
    ax.plot([planet_a[0], planet_a[0]], [planet_a[1], planet_a[1]], [planet_a[2]-1, planet_a[2]+1], color='grey')

    # Drawing the major axis
    ax.plot([prev_orbit[0][0], prev_orbit[0][int(resolution/2)]], [prev_orbit[1][0], prev_orbit[1][int(resolution/2)]],
        [prev_orbit[2][0], prev_orbit[2][int(resolution/2)]], color='grey')

    obj.draw_plane(ax, 2, 2, rot_x=25, rot_z=0, colour='blue')

    ax.plot(prev_orbit[0], prev_orbit[1], prev_orbit[2], color='tab:blue')
    ax.plot(planet_a[0], planet_a[1], planet_a[2], marker='o', markersize=2, color='red')

    ax.figure.canvas.draw_idle()
