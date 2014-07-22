from miniGL import *

e = Engine(800, 600)

t1 = Texture('./data/textures/synqera.jpg')
t2 = Texture('./data/textures/earth.jpg')
t3 = Texture('./data/textures/ifree.jpg')
t4 = Texture('./data/textures/zw.jpg')
t5 = Texture('./data/textures/ScreenShot.jpg')
t7 = Texture('./data/textures/light_metall.jpg')
nm1 = Texture('./data/nmaps/normalmap.jpg')
nm2 = Texture("./data/nmaps/chesterfield-normal.jpg")
nm3 = Texture("./data/nmaps/original.jpg")

cm1 = Texture("./data/cubemaps/cubemap_names.jpg")
cm2 = Texture("./data/cubemaps/cube_map_envir.jpg")
cm3 = Texture("./data/cubemaps/cube_map_3.jpg")
cm4 = Texture("./data/cubemaps/XOjpg.jpg")


m1 = Material('BLINN', './data/shaders/base.vsh', './data/shaders/simple_blinn.fsh')
m2 = Material('PHONG', './data/shaders/base.vsh', './data/shaders/simple_phong.fsh')
m3 = Material('BLUR', './data/shaders/blur_base.vsh', './data/shaders/blur_simple.fsh')

for x in range(-1, 2):
    for y in range(-1, 2):
        cube = geometry.cubemapped(.6, .6, .6).set_material(m1).set_texture([t7,cm4]).translate(x, y, -4)

def update(dt):
    pass
    #cub.rotate_x(dt*50).rotate_y(dt*50)

e.set_update(update)
e.loop()
