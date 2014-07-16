from miniGL import *

e = Engine(800, 600)

t1 = Texture('./data/synqera.jpg')
t2 = Texture('./data/earth.jpg')
t3 = Texture('./data/ifree.jpg')
t4 = Texture('./data/zw.jpg')
t5 = Texture('./data/ScreenShot.jpg')
t6 = Texture('./data/normalmap.jpg')
t7 = Texture('./data/Ancient_Stars.jpg')
t8 = Texture("./data/chesterfield-normal.jpg")
eye = Texture('./data/eye_texture_3_flattened-JPEG-BIG.jpg')

m1 = Material('SIMPLE', './data/shaders/base.vsh', './data/shaders/simple.fsh')
m2 = Material('BLUR', './data/shaders/blur_base.vsh', './data/shaders/blur_simple.fsh')

#back = geometry.plane(1, 1).set_material(m1).set_texture([t2, t8]).translate(0, 0, -1)
#sph = geometry.sphere(50,32).set_material(m1).set_texture([t7])

cub = geometry.cube(5,5,5).set_material(m1).set_texture([t3, t8]).translate(0,0,-15)

def update(dt):
    pass
    #cub.rotate_x(dt*50).rotate_y(dt*50)

e.set_update(update)
e.loop()
