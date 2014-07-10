from miniGL import *
import random

e = Engine(800, 600)

t1 = Texture('./data/synqera.jpg')
t2 = Texture('./data/earth.jpg')
t3 = Texture('./data/ifree.jpg')
t4 = Texture('./data/zw.jpg')
t5 = Texture('./data/ScreenShot.jpg')
t6 = Texture('./data/normalmap.jpg')
eye = Texture('./data/eye_texture_3_flattened-JPEG-BIG.jpg')

m1 = Material('SIMPLE', './data/shaders/base.vsh', './data/shaders/simple.fsh')

back = geometry.plane(1, 5).set_material(m1).set_texture([eye]).translate(0, -.25, -1).rotate_x(100)
sph = geometry.sphere(.3, 64).set_material(m1).set_texture([t2]).translate(0, 0, -1).rotate_x(180).rotate_y(5)
#sph1 = geometry.sphere(4, 10).set_material(m5).set_texture([eye,t6]).translate(5, 3, -30).rotate_x(180).rotate_y(5)
#sph2 = geometry.sphere(4, 64).set_material(m1).set_texture([eye]).translate(-5, 3, -30).rotate_x(180).rotate_y(-5)
random.seed()

def update(dt):
#    pass
    sph.rotate_x(-50 * dt).rotate_y(-10*dt).rotate_z(-5 * dt)

def mousePress(x,y):
    print "press" + x + y

def mouseMove(x,y):
    print "move", x, y

e.set_mousehandlers(mousePress, mouseMove)
e.set_update(update)
e.loop()
