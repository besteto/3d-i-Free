from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math


def display():
    glutSolidCube(1.0)


def reshape(width, height):
    pass


def keyPressed(*args):
    if args[0] == '\033':
        sys.exit()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)

    glutCreateWindow("Try work with pyOpenGL from start")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyPressed)

    glutMainLoop()


print "Hit ESC key to quit."
main()