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
nm4 = Texture("./data/nmaps/cubenm.jpg")

cm1 = Texture("./data/cubemaps/cubemap_names.jpg")
cm2 = Texture("./data/cubemaps/cube_map_envir.jpg")
cm3 = Texture("./data/cubemaps/cube_map_3.jpg")
cm4 = Texture("./data/cubemaps/XO.jpg")


m1 = Material('BLINN', './data/shaders/base.vsh', './data/shaders/simple_blinn.fsh')
m2 = Material('PHONG', './data/shaders/base.vsh', './data/shaders/simple_phong.fsh')
m3 = Material('BLUR', './data/shaders/blur_base.vsh', './data/shaders/blur_simple.fsh')

cubes = []

for x in xrange(-1, 2):
    for y in xrange(-1, 2):
        cube = geometry.cubemapped(.6, .6, .6).set_material(m1).set_texture([cm4,nm4]).translate(x, y, -4)
        cubes.append(cube)

def update(dt):
    #pass
    for everyC in cubes:
        everyC.rotate_y(dt*50)

def mmove(mx, my):
    dx = mx - e.prevMouse[0]
    dy = my - e.prevMouse[1]
    e.prevMouse = [mx, my]
    for every in cubes:
        every.rotate_y(dx)
        every.rotate_x(dy)

def mclick(GLUT_RIGHT_BUTTON, GLUT_UP, mx,my):
    if (len(cubes) == 9):
        cubes.pop(8).rotate_x(-90)
    elif (len(cubes) == 8):
        cubes.pop(4).rotate_x(-90)
    elif (len(cubes) == 7):
        cubes.pop(0).rotate_x(-90)



e.set_mousehandlers(mmove, mclick)
e.set_update(update)
e.loop()
