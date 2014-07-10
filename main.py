from miniGL import *

e = Engine(800, 600)

t1 = Texture('./data/synqera.jpg')
t2 = Texture('./data/earth.jpg')
t3 = Texture('./data/ifree.jpg')
t4 = Texture('./data/zw.jpg')
t5 = Texture('./data/ScreenShot.jpg')
t6 = Texture('./data/normalmap.jpg')
eye = Texture('./data/eye_texture_3_flattened-JPEG-BIG.jpg')

m1 = Material('SIMPLE', './data/shaders/base.vsh', './data/shaders/simple.fsh')
m2 = Material('BLUR', './data/shaders/blur_base.vsh', './data/shaders/blur_simple.fsh')

back = geometry.plane(1, 1).set_material(m2).set_texture([t3]).translate(0, 0, -1)

def update(dt):
    pass

e.set_update(update)
e.loop()
