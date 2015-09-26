from miniGL import *

e = Engine(800, 600)

cubemap = Texture("./data/cubemaps/XO.jpg")
normalcubemap = Texture("./data/nmaps/cubenm.jpg")
mBlinn = Material('BLINN', './data/shaders/base.vsh', './data/shaders/simple_blinn.fsh')

cubeSize = .6


class tttCube():
    __cube = None
    __state = "Def"

    def __init__(self, x, y, z):
        self.__cube = geometry.cubemapped(cubeSize, cubeSize, cubeSize).set_material(mBlinn).set_texture([cubemap,normalcubemap]).translate(x, y, z)

    def mark(self):
        self.__state = tttBoard.marker

class tttBoard():
    marker = "X"
    cubes = {}

    def __init__(self):
        for x in xrange(1, 4):
            for y in xrange(1, 4):
                cube = tttCube(x-2, y-2, -4)
                self.cubes[(x, y)] = cube

    def marked(self, cubNumb):
        self.cubes(cubNumb).mark


def update(dt):
    #pass
    for everyC in cubes:
        everyC.rotate_y(dt*50)

def mmove(mx, my):
    dx = mx - e.prevMouse[0]
    dy = my - e.prevMouse[1]
    e.prevMouse = [mx, my]
    for every in cubes:
        every.rotate_y(dx)
        every.rotate_x(dy)

def mclick(GLUT_RIGHT_BUTTON, GLUT_UP, mx, my):

    if mx/800 < 0.3:
        x = 1
    elif mx/800 < 0.6:
        x = 2
    else:
        x = 3

    if my/600 < 0.3:
        y = 1
    elif my/600 < 0.6:
        y = 2
    else:
        y = 3

    tulp = (x, y)
    tttBoard.marked(tulp)

e.set_mousehandlers(mmove, mclick)
e.set_update(update)
e.loop()