from OpenGL.GL import *
from OpenGL.GLU import *

def draw_grid(area, step, color=(0.3,0.3,0.3)):
    glBegin(GL_LINES)
    glColor3f(*color)
    for y in range(-area, area, step):
        glVertex3f(-area, y, 0)
        glVertex3f(area, y, 0)
    for x in range(-area, area, step):
        glVertex3f(x, -area, 0)
        glVertex3f(x, area, 0)
    glEnd()