from miniGL import *

e = Engine(800, 600)

t1 = Texture('./data/synqera.jpg')
t2 = Texture('./data/earth.jpg')
t3 = Texture('./data/ifree.jpg')
t4 = Texture('./data/zw.jpg')
t5 = Texture('./data/ScreenShot.jpg')
t6 = Texture('./data/normalmap.jpg')
eye = Texture('./data/eye_texture_3_flattened-JPEG-BIG.jpg')

m1 = Material('BLINK', './data/shaders/base.vsh', './data/shaders/blink.fsh')
m2 = Material('PLASMA',  './data/shaders/base.vsh', './data/shaders/light_plasma.fsh')
m3 = Material('BLUR', './data/shaders/blur_base.vsh', './data/shaders/blur_simple.fsh')
m4 = Material('ALPHA_BLINK', './data/shaders/base.vsh', './data/shaders/alpha_blink.fsh')

m5 = Material('BUMP_LOL', './data/shaders/base.vsh', './data/shaders/bump_lol.fsh')

back = geometry.plane(64, 64).set_material(m5).set_texture([t2,t6]).translate(0, 0, -80)
cub = geometry.cube(15,15,15).set_material(m5).set_texture([t2,t6]).translate(0,0,-50)
sph1 = geometry.sphere(4, 10).set_material(m5).set_texture([eye,t6]).translate(5, 3, -30).rotate_x(180).rotate_y(5)
sph2 = geometry.sphere(4, 64).set_material(m1).set_texture([eye]).translate(-5, 3, -30).rotate_x(180).rotate_y(-5)

def update(dt):
#    pass
     cub.rotate_x(-50 * dt).rotate_y(-10*dt)

e.set_update(update)
e.loop()
