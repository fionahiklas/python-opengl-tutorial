import time
import sys
import OpenGL

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
)


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

# change view angle, exit upon ESC
def key(k, x, y):
    global view_rotz

    if k == 'z':
        view_rotz += 5.0
    elif k == 'Z':
        view_rotz -= 5.0
    elif ord(k) == 27: # Escape
        sys.exit(0)
    else:
        return
    glutPostRedisplay()


def draw():
    glRotatef(1, 3, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    Cube()
    glutSwapBuffers()


def visible(vis):
    if vis == GLUT_VISIBLE:
        glutIdleFunc(idle)
    else:
        glutIdleFunc(None)


def idle():
    glutPostRedisplay()


def init():
    glEnable(GL_NORMALIZE)


if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)

    glutInitWindowPosition(0, 0)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Cube")
    init()

    display = (800,600)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)

    glutDisplayFunc(draw)
    #glutReshapeFunc(reshape)
    glutKeyboardFunc(key)
    #glutSpecialFunc(special)
    glutVisibilityFunc(visible)

    if "-info" in sys.argv:
        print "GL_RENDERER   = ", glGetString(GL_RENDERER)
        print "GL_VERSION    = ", glGetString(GL_VERSION)
        print "GL_VENDOR     = ", glGetString(GL_VENDOR)
        print "GL_EXTENSIONS = ", glGetString(GL_EXTENSIONS)

    glutMainLoop()

