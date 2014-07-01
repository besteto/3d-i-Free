from miniGL import *

e = Engine(800, 600)

t1 = Texture('./data/synqera.jpg')
t2 = Texture('./data/earth.jpg')
t3 = Texture('./data/ifree.jpg')
t4 = Texture('./data/zw.jpg')
eye = Texture('./data/eye_texture_3_flattened-JPEG-BIG.jpg')

m1 = Material('SIMPLE', './data/shaders/base.vsh', './data/shaders/blink.fsh')
m2 = Material('STARS',  './data/shaders/base.vsh', './data/shaders/plasma.fsh')

back = geometry.plane(80, 60).set_material(m2).set_texture([t4]).translate(0, 0, -80)

sph1 = geometry.sphere(4, 64).set_material(m1).set_texture([eye]).translate(5, 0, -30).rotate_x(180).rotate_y(5)
sph2 = geometry.sphere(4, 64).set_material(m1).set_texture([eye]).translate(-5, 0, -30).rotate_x(180).rotate_y(-5)


def update(dt):
    pass
#    sph.rotate_x(-50 * dt)

e.set_update(update)
e.loop()
