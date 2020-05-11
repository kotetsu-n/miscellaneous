from OpenGL.GL import *
from OpenGL.GLU import *

def draw_cube(size):
    half = size * 0.5
    # bottom
    glBegin(GL_QUADS)
    glColor3f(1, 0, 0)
    glVertex3f(-half, -half, -half)
    glVertex3f(-half, half, -half)
    glVertex3f(half, half, -half)
    glVertex3f(half, -half, -half)
    # top
    glColor3f(0,1,0)
    glVertex3f(-half, -half, half)
    glVertex3f(-half, half, half)
    glVertex3f(half, half, half)
    glVertex3f(half, -half, half)

    #x-
    glColor3f(0,0,1)
    glVertex3f(-half, -half, -half)
    glVertex3f(-half, half, -half)
    glVertex3f(-half, half, half)
    glVertex3f(-half, -half, half)

    #x+
    glColor3f(1,1,0)
    glVertex3f(half, half, -half)
    glVertex3f(half, -half, -half)
    glVertex3f(half, -half, half)
    glVertex3f(half, half, half)

    #y-
    glColor3f(0,1,1)
    glVertex3f(-half, -half, -half)
    glVertex3f(half, -half, -half)
    glVertex3f(half, -half, half)
    glVertex3f(-half, -half, half)

    #y+
    glColor3f(1,0,1)
    glVertex3f(-half, half, -half)
    glVertex3f(-half, half, half)
    glVertex3f(half, half, half)
    glVertex3f(half, half, -half)
    glEnd()

def draw_cube_wire(size):
    half = size * 0.5
    glLineWidth(size)
    # bottom
    glBegin(GL_LINES)
    glColor3f(1, 1, 1)
    glVertex3f(-half, -half, -half)
    glVertex3f(-half, half, -half)
    
    glVertex3f(-half, half, -half)
    glVertex3f(half, half, -half)
    
    glVertex3f(half, half, -half)
    glVertex3f(half, -half, -half)
    
    glVertex3f(half, -half, -half)
    glVertex3f(-half, -half, -half)
    # top
    glVertex3f(-half, -half, half)
    glVertex3f(-half, half, half)
    
    glVertex3f(-half, half, half)
    glVertex3f(half, half, half)
    
    glVertex3f(half, half, half)
    glVertex3f(half, -half, half)
    
    glVertex3f(half, -half, half)
    glVertex3f(-half, -half, half)

    #x-
    glVertex3f(-half, -half, -half)
    glVertex3f(-half, half, -half)
    
    glVertex3f(-half, half, -half)
    glVertex3f(-half, half, half)
    
    glVertex3f(-half, half, half)
    glVertex3f(-half, -half, half)
    
    glVertex3f(-half, -half, half)
    glVertex3f(-half, -half, -half)
    
    #x+
    glVertex3f(half, half, -half)
    glVertex3f(half, -half, -half)
    
    glVertex3f(half, -half, -half)
    glVertex3f(half, -half, half)
    
    glVertex3f(half, -half, half)
    glVertex3f(half, half, half)
    
    glVertex3f(half, half, half)
    glVertex3f(half, half, -half)
    
    #y-
    glVertex3f(-half, -half, -half)
    glVertex3f(half, -half, -half)
    
    glVertex3f(half, -half, -half)
    glVertex3f(half, -half, half)
    
    glVertex3f(half, -half, half)
    glVertex3f(-half, -half, half)
    
    glVertex3f(-half, -half, half)
    glVertex3f(-half, -half, -half)
    
    #y+
    glVertex3f(-half, half, -half)
    glVertex3f(-half, half, half)
    
    glVertex3f(-half, half, half)
    glVertex3f(half, half, half)
    
    glVertex3f(half, half, half)
    glVertex3f(half, half, -half)
    
    glVertex3f(half, half, -half)
    glVertex3f(-half, half, -half)
    glEnd()
    glLineWidth(1)