import time
from OpenGL.GL import *
from OpenGL.GLUT import *
from matrix import mat4

class Engine:
    __instance = None
    __updateFunction = None
    __keyboardFunction = None
    __objects = []
    __time = time.time()
    __delta = 0
    __prevMouse = []
    camera = None
    prevMouse = [glutGet(GLUT_WINDOW_WIDTH)/2,glutGet(GLUT_WINDOW_HEIGHT)/2]

    def __init__(self, w, h):
        print 'init miniGL {0:d}x{1:d}'.format(w, h)
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(w, h)
        glutInitWindowPosition(0, 0)
        glutCreateWindow("miniengine")
        glClearColor(0.0, 0.1, 0.1, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LEQUAL)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
        glutDisplayFunc(self.__draw)
        glutReshapeFunc(self.__resize)
        glutIdleFunc(self.__update)
        glutKeyboardFunc(self.__key)
        Engine.camera = mat4()
        Engine.__instance = self


    def __key(self, *args):
        if args[0] == '\033':
            sys.exit()
        elif self.__keyboardFunction:
            self.__keyboardFunction(args[0])

    @staticmethod
    def __resize(w, h):
        print 'resize {0:d}x{1:d}'.format(w, h)
        Engine.camera.perspective(35, float(w) / h, 0.1, 100)
        glViewport(0, 0, w, h)

    def __draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        for obj in self.__objects:
            obj.draw()
        glutSwapBuffers()

    def __update(self):
        if self.__updateFunction:
            self.__updateFunction(Engine.get_time() - self.__delta)
        self.__delta = Engine.get_time()
        glutPostRedisplay()

    def set_update(self, hdl):
        self.__updateFunction = hdl
        return self

    def set_keyhandler(self, hdl):
        self.__keyboardFunction = hdl
        return self

    def set_mousehandlers(self, mmove, mpress):
        glutMotionFunc(mmove)
        glutMouseFunc(mpress)
        return self

    @staticmethod
    def add_object(self, obj):
        self.__objects.append(obj)
        return self

    @staticmethod
    def loop():
        glutMainLoop()

    @staticmethod
    def get_time():
        t = time.time() - Engine.__time
        return t

    @staticmethod
    def get():
        return Engine.__instance
