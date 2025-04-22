import math as m
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import axes3d

import graph
import rotate as rot
import objects as obj


def render_graph(ax, e, w, i , o):
    orbit = obj.generate_ellipse(a=1, e=e)
    orbit = rot.rotate_3d(orbit, 0, 0, w % 360); orbit = rot.rotate_3d(orbit, i % 360, 0, o % 360)

    # Arrow in reference direction
    obj.draw_3d_arrow(ax, start=(0, 0, 0), direction=(2, 0, 0), length=2, color='grey')
        
    # Line between sun and centre of the ellipse
    line_c = np.array([[-e, 0], [0, 0], [0, 0]])
    line_c = rot.rotate_3d(line_c, 0, 0, w); line_c = rot.rotate_3d(line_c, i, 0, o)
    ax.plot(line_c[0], line_c[1], line_c[2], linestyle='dotted', color='black')

    # Line between sun and periapsis
    ax.plot([0, orbit[0][0]], [0, orbit[1][0]], [0, orbit[2][0]], color='black')

    # Line from the centre to the apoapsis
    ax.plot([line_c[0][0], orbit[0][180]], [line_c[1][0], orbit[1][180]], [line_c[2][0], orbit[2][180]],
        linestyle='dotted', color='grey')
        
    # Line of intersection
    if i != 0 and i != 180:
        # Line inside the orbit
        if 1 < w % 360 < 359 and not(179 <= w % 360 <= 181):
            ax.plot([0, orbit[0][0-w]], [0, orbit[1][0-w]], [0, 0], color='black')
            ax.plot([0, orbit[0][180-w]], [0, orbit[1][180-w]], [0, 0], color='black')
        # Line outside of the orbit
        dx = m.cos(m.radians(o)) + 0.00001; dy = m.sin(m.radians(o)) + 0.00001; length = min(abs(2 / dx), abs(2 / dy))
        line_i = np.array([[-dx * length, dx * length], [-dy * length, dy * length], [0, 0]])
        ax.plot([line_i[0][0], orbit[0][180-w]], [line_i[1][0], orbit[1][180-w]], line_i[2], linestyle='dotted', color='black')
        ax.plot([line_i[0][1], orbit[0][0-w]], [line_i[1][1], orbit[1][0-w]], line_i[2], linestyle='dotted', color='black')

    # Drawing the planes of referene
    obj.draw_plane(ax, 2, 2, colour='green')
    if i % 360 != 0 and i != 180:
        obj.draw_plane(ax, 2, 2, rot_x=i, rot_z=o, colour='blue')

    obj.draw_planet_and_sun(ax=ax, bahn=orbit)
    ax.plot(orbit[0], orbit[1], orbit[2], color='tab:blue')


last_angle_sum = 0
def preview_graph(updated_val, ax, prev_int, e, w, i , o):
    global last_angle_sum
    resolution = 16

    # Only render the graph if any angle has changed by at least 10°
    if abs(e * 200 + w + i + o - last_angle_sum) < prev_int and updated_val % 90 not in [0, 0.1, 0.9]:
        return
    last_angle_sum = e * 200 + w + i + o
    graph.reset_graph(ax=ax)

    prev_orbit = obj.generate_ellipse_centered(a=1, e=e, resolution=resolution)
    prev_orbit = rot.rotate_3d(prev_orbit, 0, 0, w % 360); prev_orbit = rot.rotate_3d(prev_orbit, i % 360, 0, o % 360)

    # Line of intersection
    if i % 360 != 0 and i != 180:
        dx = m.cos(m.radians(o)) + 0.00001; dy = m.sin(m.radians(o)) + 0.00001; length = min(abs(2 / dx), abs(2 / dy))
        line_i = np.array([[-dx * length, dx * length], [-dy * length, dy * length], [0, 0]])
        ax.plot(line_i[0], line_i[1], line_i[2], color='black')

    # Drawing the major axis
    ax.plot([prev_orbit[0][0], prev_orbit[0][int(resolution/2)]], [prev_orbit[1][0], prev_orbit[1][int(resolution/2)]],
        [prev_orbit[2][0], prev_orbit[2][int(resolution/2)]], color='black')

    obj.draw_plane(ax, 2, 2, colour='green')
    ax.plot(prev_orbit[0], prev_orbit[1], prev_orbit[2], color='tab:blue')  
    ax.figure.canvas.draw_idle()
