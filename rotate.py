import math as m
import numpy as np

def rotate_3d(figure, ang_x=0, ang_y=0, ang_z=0):
    # Drehmatrizen
    ROT_MAT_X = np.array([
        [1, 0, 0],
        [0, m.cos(m.radians(int(ang_x))), -m.sin(m.radians(int(ang_x)))], 
        [0, m.sin(m.radians(int(ang_x))), m.cos(m.radians(int(ang_x)))]
    ])
    ROT_MAT_Y = np.array([
        [m.cos(m.radians(int(ang_y))), 0, -m.sin(m.radians(int(ang_y)))],
        [0, 1, 0],
        [m.sin(m.radians(int(ang_y))), 0, m.cos(m.radians(int(ang_y)))]
    ])
    ROT_MAT_Z = np.array([
        [m.cos(m.radians(int(ang_z))), -m.sin(m.radians(int(ang_z))), 0],
        [m.sin(m.radians(int(ang_z))), m.cos(m.radians(int(ang_z))), 0],
        [0, 0, 1]
    ])
    
    figure = np.matmul(ROT_MAT_X, figure)
    figure = np.matmul(ROT_MAT_Y, figure)
    figure = np.matmul(ROT_MAT_Z, figure)
    return figure


def rotate_plane(x, y, z, ang_x, ang_y, ang_z):
    # Ebene drehbar machen
    plane = np.vstack((x.flatten(), y.flatten(), z.flatten()))    

    rotated_plane = rotate_3d(plane, ang_x, ang_y, ang_z)
    return rotated_plane[0].reshape(x.shape), rotated_plane[1].reshape(y.shape), rotated_plane[2].reshape(z.shape)
