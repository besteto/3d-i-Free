from miniGL import *

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
        for x in range(1, 4):
            for y in range(1, 4):
                cube = tttCube(x-2, y-2, -4)
                self.cubes[(x, y)] = cube

    def marker(self):
        pass