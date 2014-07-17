from miniGL import *

e = Engine(800, 600)

t1 = Texture('./data/textures/synqera.jpg')
t2 = Texture('./data/textures/earth.jpg')
t3 = Texture('./data/textures/ifree.jpg')
t4 = Texture('./data/textures/zw.jpg')
t5 = Texture('./data/textures/ScreenShot.jpg')
t7 = Texture('./data/textures/Ancient_Stars.jpg')
nm1 = Texture('./data/nmaps/normalmap.jpg')
nm2 = Texture("./data/nmaps/chesterfield-normal.jpg")
nm3 = Texture("./data/nmaps/original.jpg")

m1 = Material('SIMPLE', './data/shaders/base.vsh', './data/shaders/simple.fsh')
m2 = Material('BLUR', './data/shaders/blur_base.vsh', './data/shaders/blur_simple.fsh')

#back = geometry.plane(1, 1).set_material(m1).set_texture([t2, nm2]).translate(0, 0, -1)
#sph = geometry.sphere(50,32).set_material(m1).set_texture([t7])

cub = geometry.cube(5,5,5).set_material(m1).set_texture([t5, nm3]).translate(0,0,-15)

def update(dt):
    pass
    #cub.rotate_x(dt*50).rotate_y(dt*50)

e.set_update(update)
e.loop()
