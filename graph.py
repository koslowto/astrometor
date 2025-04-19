import math as m
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import axes3d

import bahnelemente as bahn
import fruehlingspunkt as frueh


# Function to reset the graph
def reset_graph(ax):
    ax.clear()
    ax.set_axis_off()
    ax.set_xlim([-2, 2]); ax.set_ylim([-2, 2]); ax.set_zlim([-1.25, 1.25])


# Function to fully render the graph
def update_graph(ax, mode, e, w, i , o, v):
    reset_graph(ax=ax)

    if mode == 'Frühlingspunkt':
        frueh.render_graph(ax=ax, v=v)
    elif mode == 'Bahnelemente':
        bahn.render_graph(ax=ax, e=e, w=w, i=i, o=o); v = 45

    ax.figure.canvas.draw_idle()


# Function to change mode between visualizing the
def change_mode(mode, ax, slider_e, slider_i, slider_o, slider_w, slider_v,
                ax_slider_e, ax_slider_i, ax_slider_o, ax_slider_w, ax_slider_v):
    if mode == 'Bahnelemente':
        ax.view_init(elev = 25, azim=-80, roll=0)
        slider_e.set_active(True)
        slider_i.set_active(True)
        slider_o.set_active(True)
        slider_w.set_active(True)
        slider_v.set_active(False)
        ax_slider_e.set_visible(True)
        ax_slider_i.set_visible(True)
        ax_slider_o.set_visible(True)
        ax_slider_w.set_visible(True)
        ax_slider_v.set_visible(False)
    elif mode == 'Frühlingspunkt':
        ax.view_init(elev = 25, azim=-5, roll=-30)
        slider_e.set_active(False)
        slider_i.set_active(False)
        slider_o.set_active(False)
        slider_w.set_active(False)
        slider_v.set_active(True)
        ax_slider_e.set_visible(False)
        ax_slider_i.set_visible(False)
        ax_slider_o.set_visible(False)
        ax_slider_w.set_visible(False)
        ax_slider_v.set_visible(True)

    update_graph(ax=ax, mode=mode, e=slider_e.val, w=slider_w.val, i=slider_i.val, o=slider_o.val, v=slider_v.val)
