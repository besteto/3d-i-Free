#
# Examples for PyOpenGL
#
# Author: Alex V. Boreskoff
#

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

angle = 0.0
angle2 = 0.0
texture = 0
object = 0
d = 3.0 / math.sqrt(3)


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LEQUAL)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)
    glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, float(width) / float(height), 1.0, 60.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 0, 1, 1, 1, 0, 1, 0)
    glTranslatef(4, 4, 4)
    glRotatef(angle2, 1, -1, 0)
    glTranslatef(d - 1.5, d - 1.5, d - 1.5)
    glTranslatef(1.5, 1.5, 1.5)  # move cube from the center
    glRotatef(angle, 1.0, 1.0, 0.0)
    glTranslatef(-1.5, -1.5, -1.5)  # move cube into the center

    glutSolidCube(2.0)

    glutSwapBuffers()


def keyPressed(*args):
    if args[0] == '\033':
        sys.exit()


def animate():
    global angle, angle2

    angle = 0.04 * glutGet(GLUT_ELAPSED_TIME)
    angle2 = 0.01 * glutGet(GLUT_ELAPSED_TIME)

    glutPostRedisplay()


def main():
    global texture

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)

    glutCreateWindow("Simple PyOpenGL examplRURURURe")
    glutDisplayFunc(display)
    glutIdleFunc(animate)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyPressed)
    init()

    glutMainLoop()


print "Hit ESC key to quit."
main()
