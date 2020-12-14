from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations
from math import sin, cos, pi


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect("auto")

# cube
r = [-1, 1]
for s, e in combinations(np.array(list(product(r, r, r))), 2):
    if np.sum(np.abs(s-e)) == r[1]-r[0]:
        ax.plot3D(*zip(s, e), color="b")


# Function to translate
def Translate(tx, ty, tz):
    for s, e in combinations(np.array(list(product(r, r, r))), 2):
        if np.sum(np.abs(s-e)) == r[1]-r[0]:
            sTranslated = [s[0] + tx, s[1] + ty, s[2] + tz]
            eTranslated = [e[0] + tx, e[1] + ty, e[2] + tz]      
            ax.plot3D(*zip(sTranslated,eTranslated), color="g")


# Function to rotate in x axis
def XRotate(angle):
    for s, e in combinations(np.array(list(product(r, r, r))), 2):
        if np.sum(np.abs(s-e)) == r[1]-r[0]:
            sRotated = [s[0], s[1] * cos(angle) - s[2] * sin(angle), s[1] * sin(angle) + s[2] * cos(angle)]
            eRotated = [e[0], e[1] * cos(angle) - e[2] * sin(angle), e[1] * sin(angle) + e[2] * cos(angle)]      
            ax.plot3D(*zip(sRotated,eRotated), color="r")


# Function to rotate in y axis
def YRotate(angle):
    for s, e in combinations(np.array(list(product(r, r, r))), 2):
        if np.sum(np.abs(s-e)) == r[1]-r[0]:
            sRotated = [s[0] * cos(angle) + s[2] * sin(angle), s[1], -s[0] * sin(angle) + s[2] * cos(angle)]
            eRotated = [e[0] * cos(angle) + e[2] * sin(angle), e[1], -e[0] * sin(angle) + e[2] * cos(angle)]      
            ax.plot3D(*zip(sRotated,eRotated), color="y")


# Function to rotate in z axis
def ZRotate(angle):
    for s, e in combinations(np.array(list(product(r, r, r))), 2):
        if np.sum(np.abs(s-e)) == r[1]-r[0]:
            sRotated = [s[0] * cos(angle) - s[1] * sin(angle), s[0] * sin(angle) + s[1] * cos(angle), s[2]]
            eRotated = [e[0] * cos(angle) - e[1] * sin(angle), e[0] * sin(angle) + e[1] * cos(angle), e[2]]      
            ax.plot3D(*zip(sRotated,eRotated), color="k")


# Function to scale
def Scale(sx, sy, sz):
    for s, e in combinations(np.array(list(product(r, r, r))), 2):
        if np.sum(np.abs(s-e)) == r[1]-r[0]:
            sScaled = [s[0] * sx, s[1] * sy, s[2] * sz]
            eScaled = [e[0] * sx, e[1] * sy, e[2] * sz]      
            ax.plot3D(*zip(sScaled,eScaled), color="m")


# # sphere
# u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
# x = np.cos(u)*np.sin(v)
# y = np.sin(u)*np.sin(v)
# z = np.cos(v)
# ax.plot_wireframe(x, y, z, color="r")

Translate(2, 2, 2)
XRotate(pi/4)
YRotate(pi/4)
ZRotate(pi/4)
Scale(2, 2, 2)

plt.show()
