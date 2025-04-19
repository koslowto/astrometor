import math as m
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import axes3d

import graph
import rotate as rot
import objects as obj

# Create the orbit
orbit = obj.generate_ellipse_centered(a=1, e=0, resolution=360)
orbit = rot.rotate_3d(orbit, 0, 0, 90); orbit = rot.rotate_3d(orbit, 25, 0, 0)

# Funktion zur Vorschau der Planetenbahn im Frühlingspunkt-Modus
def render_graph(ax, v):
    global orbit

    # Wenn der Planet sich im *punkt befindet, Vektor zum *punkt zeichnen
    if 88 <= v <= 92 or 268 <= v <= 272:
        ax.plot([orbit[0][270], orbit[0][90]], [orbit[1][270], orbit[1][90]],
            [orbit[2][270], orbit[2][90]], color='red') 
        obj.draw_arrow_frueh(ax=ax, v=v)
    else: # Schnittlinie von Planetenbahn und Bezugsebnene zeichnen
        ax.plot([orbit[0][270], orbit[0][90]], [orbit[1][270], orbit[1][90]],
            [orbit[2][270], orbit[2][90]], color='black')
        ax.plot([-2, 2], [0, 0], [0, 0], linestyle='dotted', color='black')

    # Planetenachse zeichnen
    planet_a = [m.cos(m.radians(v)), m.sin(m.radians(v)), 0]
    planet_a = rot.rotate_3d(planet_a, 0, 0, 90); planet_a = rot.rotate_3d(planet_a, 25, 0, 0)
    ax.plot(planet_a[0], planet_a[1], [planet_a[2]-1, planet_a[2]+1], color='grey')
     
    # Große Halbachse zeichnen
    ax.plot([orbit[0][0], orbit[0][180]], [orbit[1][0], orbit[1][180]],
        [orbit[2][0], orbit[2][180]], linestyle='dotted', color='grey')

    # Bahnebene zeichnen 
    obj.draw_plane(ax, 2, 2, rot_x=25, rot_z=0, colour='blue')
    # Bezugsebene zeichnen
    obj.draw_plane(ax, 2, 2, rot_x=0, rot_z=0, colour='green')

    # Planeten und Sonne zeichnen
    obj.draw_planet_and_sun(ax=ax, bahn=orbit, v=v)

    # Planetenbahn zeichnen
    ax.plot(orbit[0], orbit[1], orbit[2], color='tab:blue')



# Planetenbahn für den Frühlingspunkt erstellen
last_angle = 0; resolution = 16; t = np.arange(0, resolution + 1) 
prev_orbit = np.array([np.cos(np.radians(360 / resolution * t)),np.sin(np.radians(360 / resolution * t)),[0] * (resolution + 1)])
prev_orbit = rot.rotate_3d(prev_orbit, 0, 0, 90); prev_orbit = rot.rotate_3d(prev_orbit, 25, 0, 0)

# Funktion zur Vorschau der Planetenbahn im Frühlingspunkt-Modus
def preview_graph(ax, v):
    global prev_orbit
    global resolution
    global last_angle

    # Der Graph wird aus Performance-Gründen nur gezeichnet, wenn
    #  sich der Winkel v um mindesten 10° verändert hat oder der Planet sich vom *punkt entfernt
    #  oder der Planet sich im *punkt befindet (setzen sie (Herbst|Frühling) für '*' ein :])
    if not (88 <= v <= 92 or 268 <= v <= 272):
        if abs(v - last_angle) < 10 and not (88 <= last_angle <= 92 or 268 <= last_angle <= 272):
            return
    last_angle = v
    graph.reset_graph(ax=ax)

    # Wenn der Planet sich im *punkt befindet, Vektor zum *punkt zeichnen
    if 88 <= v <= 92 or 268 <= v <= 272:
        ax.plot([prev_orbit[0][3*int(resolution/4)], prev_orbit[0][int(resolution/4)]], [prev_orbit[1][3*int(resolution/4)],
            prev_orbit[1][int(resolution/4)]], [prev_orbit[2][3*int(resolution/4)], prev_orbit[2][int(resolution/4)]], color='red') 
        obj.draw_arrow_frueh(ax=ax, v=v)
    else: # Schnittlinie von Planetenbahn und Bezugsebnene zeichnen
        ax.plot([prev_orbit[0][3*int(resolution/4)], prev_orbit[0][int(resolution/4)]], [prev_orbit[1][3*int(resolution/4)],
            prev_orbit[1][int(resolution/4)]], [prev_orbit[2][3*int(resolution/4)], prev_orbit[2][int(resolution/4)]], color='grey')

    # Planetenachse zeichnen
    planet_a = [m.cos(m.radians(v)), m.sin(m.radians(v)), 0]
    planet_a = rot.rotate_3d(planet_a, 0, 0, 90); planet_a = rot.rotate_3d(planet_a, 25, 0, 0)
    ax.plot(planet_a[0], planet_a[1], [planet_a[2]-1, planet_a[2]+1], color='grey')

    # Große Halbachse zeichnen
    ax.plot([prev_orbit[0][0], prev_orbit[0][int(resolution/2)]], [prev_orbit[1][0], prev_orbit[1][int(resolution/2)]],
        [prev_orbit[2][0], prev_orbit[2][int(resolution/2)]], color='grey')

    # Bahnebene zeichnen 
    obj.draw_plane(ax, 2, 2, rot_x=25, rot_z=0, colour='blue')

    # Planetenbahn zeichnen
    ax.plot(prev_orbit[0], prev_orbit[1], prev_orbit[2], color='tab:blue')
    ax.plot(planet_a[0], planet_a[1], planet_a[2], marker='o', markersize=2, color='red')
    ax.figure.canvas.draw_idle()
