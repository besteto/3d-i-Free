import miniengine
import objects
import shaders

e = miniengine.Engine(800, 600)

e.add_object(objects.plane(40,40).set_material(shaders.water()).translate(0, 0, -60))
cube = objects.cube(.6, .6, .6).set_material(shaders.newbie()).translate(0, 0, -4)
e.add_object(cube)

def update(dt):
    cube.rotate_x(45 * dt).rotate_z(45 * dt)

e.set_update(update)
e.loop()