from mesh import Mesh
from math import *


def plane(width, height):
    w = float(width) / 2.0
    h = float(height) / 2.0
    return Mesh([
                    -w, h, 0,   0, 1,   0, 0, 1,    0, 1, 0,    1, 0, 0,
                    -w, -h, 0,  0, 0,   0, 0, 1,    0, 1, 0,    1, 0, 0,
                    w, -h, 0,   1, 0,   0, 0, 1,    0, 1, 0,    1, 0, 0,
                    w, h, 0,    1, 1,   0, 0, 1,   0, 1, 0,    1, 0, 0,
                ],
                [0, 1, 3, 2, 3, 1])


def cube(a, b, c):
    ax = a / 2.0
    by = b / 2.0
    cz = c / 2.0
    return Mesh(
        [
            #coord          ux      normal(z)  binormal(y)  tangent(x)
            #front 0-3
            -ax, -by, cz,   0, 0,   0, 0, 1,    0, 1, 0,    1, 0, 0,
            -ax, by, cz,    0, 1,   0, 0, 1,    0, 1, 0,    1, 0, 0,
            ax, -by, cz,    1, 0,   0, 0, 1,    0, 1, 0,    1, 0, 0,
            ax, by, cz,     1, 1,   0, 0, 1,    0, 1, 0,    1, 0, 0,

            #top 4-7
            -ax, by, cz,    0, 0,   0, 1, 0,    0, 0, 1,    1, 0, 0,
            ax, by, cz,     1, 0,   0, 1, 0,    0, 0, 1,    1, 0, 0,
            -ax, by, -cz,   0, 1,   0, 1, 0,    0, 0, 1,    1, 0, 0,
            ax, by, -cz,    1, 1,   0, 1, 0,    0, 0, 1,    1, 0, 0,

            #right 8-11
            ax, -by, cz,    0, 0,   1, 0, 0,    0, 1, 0,    0, 0, 1,
            ax, by, cz,     0, 1,   1, 0, 0,    0, 1, 0,    0, 0, 1,
            ax, -by, -cz,   1, 0,   1, 0, 0,    0, 1, 0,    0, 0, 1,
            ax, by, -cz,    1, 1,   1, 0, 0,    0, 1, 0,    0, 0, 1,

            #back 12-15
            ax, -by, -cz,   0, 0,   0, 0, -1,
            ax, by, -cz,    0, 1,   0, 0, -1,
            ax, -by, -cz,   1, 0,   0, 0, -1,
            -ax, by, -cz,   1, 1,   0, 0, -1,

            #bottom 16-19
            -ax, -by, cz,    0, 0,   0, -1, 0,
            ax, -by, cz,     1, 0,   0, -1, 0,
            -ax, -by, -cz,   0, 1,   0, -1, 0,
            ax, -by, -cz,    1, 1,   0, -1, 0,

            #left 20-23
            -ax, -by, cz,    1, 0,   -1, 0, 0,
            -ax, by, cz,     1, 1,   -1, 0, 0,
            -ax, -by, -cz,   0, 0,   -1, 0, 0,
            -ax, by, -cz,    0, 1,   -1, 0, 0,

        ],
        [0, 3, 1, 0, 2, 3,
         4, 7, 5, 4, 6, 7,
         8, 11, 9, 8, 10, 11,
         12, 15, 13, 12, 14, 15,
         16, 19, 17, 16, 18, 19,
         20, 23, 21, 20, 22, 23]


    )


def sphere(radius, slices):
    step = (pi * 2) / float(slices)
    parallels = slices / 2
    r = radius / 1.5
    v = []
    n = []
    for i in range(0, parallels + 1, 1):
        for j in range(0, slices + 1, 1):
            x = r * sin(step * i) * sin(step * j)
            y = r * cos(step * i)
            z = r * sin(step * i) * cos(step * j)
            v.append([x, y, z, j / float(slices), i / float(parallels), x / r, y / r, z / r])
    for i in range(0, slices / 2, 1):
        for j in range(0, slices, 1):
            n.append((i * (slices + 1) + j))
            n.append(((i + 1) * (slices + 1) + j))
            n.append(((i + 1) * (slices + 1) + (j + 1)))
            n.append((i * (slices + 1) + j))
            n.append(((i + 1) * (slices + 1) + (j + 1)))
            n.append((i * (slices + 1) + (j + 1)))
    return Mesh(v, n)


