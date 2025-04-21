import math as m
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import axes3d
from matplotlib.widgets import Slider
from matplotlib.widgets import RadioButtons

import graph
import parse_config as conf
import orbital_nodes as nodes
import orbital_elements as elem


#with open(config_path, 'r') as conf_file:
#    config = json.load(conf_file)
    #print(conf_file.readline())
#    print(config)
config = conf.parse_config()
prev_int = config["preview_interval"]

# Initialize the program
fig = plt.figure(num='AstroMetor')
plt.get_current_fig_manager().toolbar.hide()
# Configuring the graph
ax = plt.axes(projection='3d')
ax.view_init(elev = 25, azim = -80)
ax.set_xlim([-2, 2]); ax.set_ylim([-2, 2]); ax.set_zlim([-1.25, 1.25])


# UI-ELEMENTS (Sliders & Buttons)

# Slider to control the eccentricity
ax_slider_e = plt.axes([0.9, 0.25, 0.05, 0.6])
slider_e = Slider(ax_slider_e, "e", valmin = 0.1, valmax = 0.9, valinit = config["sliders"]["e"], valstep = 0.01, orientation='vertical')

# Slider to cotrol the inclination
ax_slider_i = plt.axes([0.825, 0.25, 0.05, 0.6])
slider_i = Slider(ax_slider_i, "i", valmin = 0, valmax = 360, valinit = config["sliders"]["i"], valstep = 1, orientation='vertical')

# Slider to control the longitude of the ascending node
ax_slider_o = plt.axes([0.1, 0.1, 0.8, 0.05])
slider_o = Slider(ax_slider_o, "Ω", valmin = 0, valmax = 360, valinit = config["sliders"]["o"], valstep = 1)

# Slider to control the argument of periapsis
ax_slider_w = plt.axes([0.1, 0.025, 0.8, 0.05])
slider_w = Slider(ax_slider_w, "ω", valmin = 0, valmax = 360, valinit = config["sliders"]["w"], valstep = 1)

# Slider to control the true anomaly 
ax_slider_v = plt.axes([0.1, 0.025, 0.8, 0.05])
slider_v = Slider(ax_slider_v, "ν", valmin = 0, valmax = 360, valinit = config["sliders"]["v"], valstep = 1)
slider_v.set_active(False); ax_slider_v.set_visible(False)

# Callback-Functions
slider_e.on_changed(lambda val: elem.preview_graph(ax=ax, e=slider_e.val, w=slider_w.val, i=slider_i.val, o=slider_o.val, prev_int=prev_int))
slider_i.on_changed(lambda val: elem.preview_graph(ax=ax, e=slider_e.val, w=slider_w.val, i=slider_i.val, o=slider_o.val, prev_int=prev_int))
slider_w.on_changed(lambda val: elem.preview_graph(ax=ax, e=slider_e.val, w=slider_w.val, i=slider_i.val, o=slider_o.val, prev_int=prev_int))
slider_o.on_changed(lambda val: elem.preview_graph(ax=ax, e=slider_e.val, w=slider_w.val, i=slider_i.val, o=slider_o.val, prev_int=prev_int))
slider_v.on_changed(lambda val: nodes.preview_graph(ax=ax, v=slider_v.val, prev_int=prev_int))

# Button to change the program's mode
ax_radio = plt.axes([-0.025, 0.175, 0.25, 0.1])
check = RadioButtons(ax=ax_radio, labels=list(config["labels"].keys()), activecolor='grey')
# Callback-Function
check.on_clicked(lambda val: graph.change_mode(ax=ax, mode=config["labels"][check.value_selected], 
    slider_e=slider_e, slider_w=slider_w, slider_i=slider_i, slider_o=slider_o, slider_v=slider_v, 
    ax_slider_e=ax_slider_e, ax_slider_w=ax_slider_w, ax_slider_i=ax_slider_i, ax_slider_o=ax_slider_o, ax_slider_v=ax_slider_v))


# Render the full graph only once the slider is released, otherwise just a preview
fig.canvas.mpl_connect('button_release_event', lambda event:
    graph.update_graph(mode=config["labels"][check.value_selected],
                       e=slider_e.val, w=slider_w.val, i=slider_i.val, o=slider_o.val, v=slider_v.val, ax=ax))


# Render the graph on program startup
#graph.update_graph(ax, mode=check.value_selected, e=slider_e.val, w=slider_w.val, i=slider_i.val, o=slider_o.val, v=slider_v.val)
graph.change_mode(ax=ax, mode=config["labels"][check.value_selected], 
    slider_e=slider_e, slider_w=slider_w, slider_i=slider_i, slider_o=slider_o, slider_v=slider_v, 
    ax_slider_e=ax_slider_e, ax_slider_w=ax_slider_w, ax_slider_i=ax_slider_i, ax_slider_o=ax_slider_o, ax_slider_v=ax_slider_v)
plt.show()
