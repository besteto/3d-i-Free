from miniGL import *

e = Engine(800, 600)

t1 = Texture('./data/synqera.jpg')
t2 = Texture('./data/ifree.jpg')
m1 = Material('SIMPLE', './data/shaders/base.vsh', './data/shaders/simple.fsh')

e.add_object(geometry.plane(40, 40).set_material(m1).translate(0, 0, -60).set_texture([t1]))

spheres = []
for x in range(-1, 2):
    for y in range(-1, 2):
        spher = geometry.sphere(.6, 32).set_material(m1).translate(x, y, -5).set_texture([t1])
        if y == 0:
            spher.set_material(m1).set_texture([t2])
        spheres.append(spher)
        e.add_object(spher)


def update(dt):
    for spher in spheres:
        spher.rotate_z(45 * dt).rotate_x(45 * dt)


e.set_update(update)
e.loop()
