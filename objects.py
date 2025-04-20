import math as m
import numpy as np
import rotate as rot
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def generate_ellipse(a, e, resolution=360):
    epsilon = e/a
    t = np.arange(0, resolution + 1) 
    ellipse = np.array([
        np.cos(np.radians(360 / resolution * t)) * a * ((1 - epsilon**2) / (1 + np.cos(np.radians(360 / resolution * t)) * epsilon)),
        np.sin(np.radians(360 / resolution * t)) * a * ((1 - epsilon**2) / (1 + np.cos(np.radians(360 / resolution * t)) * epsilon)),
        [0] * (resolution + 1)
    ])
    return ellipse

def generate_ellipse_centered(a, e, resolution=360):
    t = np.arange(0, resolution + 1) 
    ellipse = np.array([
        np.cos(np.radians(360 / resolution * t)) - e,
        np.sin(np.radians(360 / resolution * t)) * m.sqrt(1-e**2),
        [0] * (resolution + 1)
    ])
    return ellipse


def generate_sphere(resolution, r=1, pos_x=0, pos_y=0, pos_z=0):
    theta = np.linspace(0, 2 * np.pi, 2 * resolution)
    phi = np.linspace(0, np.pi, resolution)
    theta, phi = np.meshgrid(theta, phi)

    x = r * np.sin(phi) * np.cos(theta) + pos_x
    y = r * np.sin(phi) * np.sin(theta) + pos_y
    z = r * np.cos(phi) + pos_z

    return x, y , z


def draw_planet_and_sun(ax, bahn, v=45):
    sun_x, sun_y, sun_z = generate_sphere(resolution=6, r=0.075)
    ax.plot_surface(sun_x, sun_y, sun_z, color='yellow')

    planet_x, planet_y, planet_z = generate_sphere(resolution=5,r=0.05, pos_x=bahn[0][v], pos_y=bahn[1][v], pos_z=bahn[2][v])
    ax.plot_surface(planet_x, planet_y, planet_z, color='blue')


def draw_plane(ax, size_x, size_y, rot_x=0, rot_y=0, rot_z=0, colour='black'): 
    x, y = np.meshgrid(np.arange(-size_x, size_x+0.1, 0.1), np.arange(-size_y, size_y+0.1, 0.1)); z = 0 * x + 0 * y

    x_rot, y_rot, z_rot = rot.rotate_plane(x, y, z, rot_x, rot_y, rot_z)

    ax.plot_surface(x_rot, y_rot, z_rot, color=colour, alpha=0.125)


def draw_arrow_node(ax, v):
    # Ascending node
    if 88 <= v <= 92: 
        draw_3d_arrow(ax, start=(0, 0, 0), direction=(2, 0, 0), length=2, color='red')
    # Descending noe
    elif 268 <= v <= 272:
        draw_3d_arrow(ax, start=(0, 0, 0), direction=(-2, 0, 0), length=2, color='red')

def draw_3d_arrow(ax, start, direction, length=1.0, shaft_ratio=0.8, cone_radius=0.05, cone_height=0.2, color='blue'):
    start = np.array(start)
    direction = np.array(direction)
    direction = direction / np.linalg.norm(direction)
    
    shaft_length = length * shaft_ratio
    shaft_end = start + direction * shaft_length
    ax.plot([start[0], shaft_end[0]],
            [start[1], shaft_end[1]],
            [start[2], shaft_end[2]], color=color)

    cone_base_center = shaft_end
    cone_tip = start + direction * length

    def orthonormal_basis(v):
        if np.allclose(v, [0, 0, 1]):
            ortho = np.array([1, 0, 0])
        else:
            ortho = np.cross(v, [0, 0, 1])
        ortho = ortho / np.linalg.norm(ortho)
        b = np.cross(v, ortho)
        return ortho, b

    ortho1, ortho2 = orthonormal_basis(direction)
    theta = np.linspace(0, 2*np.pi, 20)
    circle_points = [cone_base_center + cone_radius * (np.cos(t)*ortho1 + np.sin(t)*ortho2) for t in theta]

    faces = [[cone_tip, circle_points[i], circle_points[i+1]] for i in range(len(circle_points)-1)]
    faces.append([cone_tip, circle_points[-1], circle_points[0]])
    cone = Poly3DCollection(faces, color=color, alpha=1)
    ax.add_collection3d(cone)
