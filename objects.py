from miniengine import *
from math import *


def plane(width, height):
    w = float(width) / 2.0
    h = float(height) / 2.0
    return Mesh(
        [
            -w,  h, 0.0,    0.0, 0.0,
            -w, -h, 0.0,    0.0, 1.0,
             w, -h, 0.0,    1.0, 1.0,
             w,  h, 0.0,    1.0, 0.0
        ],
        [0, 1, 3, 2, 3, 1])


def triangle(radius):
    y = float(radius) * -sin(degrees(30))
    x = float(radius) * cos(degrees(30))
    return Mesh(
        [
            -x,   -y,   0.0,  0.0, 0.0,
             x,   -y,   0.0,  0.0, 1.0,
            .0, radius, 0.0,  0.5, 1.0
        ],
        [0, 1, 2])

def flag(width):
    half = float(width) / 2.0
    quart = float(width) / 4.0

    return Mesh(
        [
            -half,  half,   0.0,    0.0, 0.0,
            -half, -half,   0.0,    0.0, 1.0,
            quart,  0.0,    0.0,    0.75,0.5,
            half,  -half,   0.0,    1.0, 1.0,
            half,   half,   0.0,    1.0, 0.0
        ],
        [4, 0, 2, 0, 2, 1, 3, 2, 1])