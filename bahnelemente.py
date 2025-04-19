import math as m
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import axes3d

import graph
import rotate as rot
import objects as obj


# Function to render the full graph
def render_graph(ax, e, w, i , o):
    orbit = obj.generate_ellipse(a=1, e=e)
    orbit = rot.rotate_3d(orbit, 0, 0, w % 360); orbit = rot.rotate_3d(orbit, i % 360, 0, o % 360)

    # Pfeil zum Frühlingspunkt zeichnen
    obj.draw_3d_arrow(ax, start=(0, 0, 0), direction=(2, 0, 0), length=2, color='grey')
        
    # Linie zwischen Sonne und Mittelpunkt
    line_m = np.array([[-e, 0], [0, 0], [0, 0]])
    line_m = rot.rotate_3d(line_m, 0, 0, w); line_m = rot.rotate_3d(line_m, i, 0, o)
    ax.plot(line_m[0], line_m[1], line_m[2], linestyle='dotted', color='black')

    #Linie zwischen Mittlepunkt und Aphel
    ax.plot([line_m[0][0], orbit[0][180]], [line_m[1][0], orbit[1][180]], [line_m[2][0], orbit[2][180]],
        linestyle='dotted', color='grey')

    # Linie zwischen Sonne und Perihel
    ax.plot([0, orbit[0][0]], [0, orbit[1][0]], [0, orbit[2][0]], color='black')
        
    # Schnittlinie der beiden Ebenen
    if i != 0 and i != 180:
        # Teil innerhalb der Bahn
        if 1 < w % 360 < 359 and not(179 <= w % 360 <= 181):
            ax.plot([0, orbit[0][0-w]], [0, orbit[1][0-w]], [0, 0], color='black')
            ax.plot([0, orbit[0][180-w]], [0, orbit[1][180-w]], [0, 0], color='black')
        # Teil außerhalb der Bahn, wird ermittelt, indem man eine Linie im Wikel o zum Frühlingspunkt stehend, bis zum Rand zeichnet (siehe unten)
        dx = m.cos(m.radians(o)) + 0.00001; dy = m.sin(m.radians(o)) + 0.00001; length = min(abs(2 / dx), abs(2 / dy))
        line_s = np.array([[-dx * length, dx * length], [-dy * length, dy * length], [0, 0]])
        ax.plot([line_s[0][0], orbit[0][180-w]], [line_s[1][0], orbit[1][180-w]], line_s[2], linestyle='dotted', color='black')
        ax.plot([line_s[0][1], orbit[0][0-w]], [line_s[1][1], orbit[1][0-w]], line_s[2], linestyle='dotted', color='black')

    # Zeichnen der Bezugsebene und der Bahnebene
    obj.draw_plane(ax, 2, 2, colour='green')
    if i % 360 != 0 and i != 180:
        obj.draw_plane(ax, 2, 2, rot_x=i, rot_z=o, colour='blue')

    # Planeten und Sonne zeichnen
    obj.draw_planet_and_sun(ax=ax, bahn=orbit)

    # Zeichnen der Bahn
    ax.plot(orbit[0], orbit[1], orbit[2], color='tab:blue')


# Funktion zur Vorschau des Graphen im Bahnelemente-Modus
last_angle_sum = 0
def preview_graph(ax, e, w, i , o):
    global last_angle_sum
    resolution = 16

    # Der Graph wird nur gerendert, wenn sich einer der Winkel um mindestens 10° verändert hat
    if abs(e * 200 + w + i + o - last_angle_sum) < 10:
        return
    last_angle_sum = e * 200 + w + i + o
    graph.reset_graph(ax=ax)

    # Bahn mit geringer Auflösung erstellen. Die Bahn wird vom Zentrum aus erstellt, damit sie gleichmößig ist
    prev_orbit = obj.generate_ellipse_centered(a=1, e=e, resolution=resolution)
    prev_orbit = rot.rotate_3d(prev_orbit, 0, 0, w % 360); prev_orbit = rot.rotate_3d(prev_orbit, i % 360, 0, o % 360)

    # Schnittlinie von Bahn und Bezugsebene einzeichnen, wenn die Bahn geneigt ist
    if i % 360 != 0 and i != 180:
        # (Die Länge der Linie bis zum Rand der Bezugsebene wird ermittelt, indem man schaut,
        #  mit welchem x man den cosinus bzw. sinus, des für diese Linie relaventen Winkels, multiplizieren müsste, um 2 zu erreichen.
        #  Dies ist die ursprüngliche Distanz zur Kante)
        dx = m.cos(m.radians(o)) + 0.00001; dy = m.sin(m.radians(o)) + 0.00001; length = min(abs(2 / dx), abs(2 / dy))
        line_s = np.array([[-dx * length, dx * length], [-dy * length, dy * length], [0, 0]])
        ax.plot(line_s[0], line_s[1], line_s[2], color='black')

    # Große Halbachse zeichnen
    ax.plot([prev_orbit[0][0], prev_orbit[0][int(resolution/2)]], [prev_orbit[1][0], prev_orbit[1][int(resolution/2)]],
        [prev_orbit[2][0], prev_orbit[2][int(resolution/2)]], color='black')

    # Bezugsebene zeichnen
    obj.draw_plane(ax, 2, 2, colour='green')

    #Bahn zeichnen
    ax.plot(prev_orbit[0], prev_orbit[1], prev_orbit[2], color='tab:blue')  
    ax.figure.canvas.draw_idle()
