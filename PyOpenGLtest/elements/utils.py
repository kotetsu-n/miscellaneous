from OpenGL.GL import *
from OpenGL.GLU import *

def define_quad(sp, ep, n):
    '''
    n = surface_normal like (1,0,0) => x+ is normal
    '''
    if n == (0,0,-1):
        glVertex3f(sp[0], sp[1], sp[2])
        glVertex3f(sp[0], ep[1], sp[2])
        glVertex3f(ep[0], ep[1], sp[2])
        glVertex3f(ep[0], sp[1], sp[2])
    elif n == (0,0,1):
        glVertex3f(sp[0], sp[1], ep[2])
        glVertex3f(sp[0], ep[1], ep[2])
        glVertex3f(ep[0], ep[1], ep[2])
        glVertex3f(ep[0], sp[1], ep[2])
    elif n == (-1,0,0):
        glVertex3f(sp[0], sp[1], sp[2])
        glVertex3f(sp[0], ep[1], sp[2])
        glVertex3f(sp[0], ep[1], ep[2])
        glVertex3f(sp[0], sp[1], ep[2])
    elif n == (1,0,0):
        glVertex3f(ep[0], ep[1], sp[2])
        glVertex3f(ep[0], sp[1], sp[2])
        glVertex3f(ep[0], sp[1], ep[2])
        glVertex3f(ep[0], ep[1], ep[2])
    elif n == (0,-1,0):
        glVertex3f(sp[0], sp[1], sp[2])
        glVertex3f(ep[0], sp[1], sp[2])
        glVertex3f(ep[0], sp[1], ep[2])
        glVertex3f(sp[0], sp[1], ep[2])
    elif n == (0,1,0):
        glVertex3f(sp[0], ep[1], sp[2])
        glVertex3f(sp[0], ep[1], ep[2])
        glVertex3f(ep[0], ep[1], ep[2])
        glVertex3f(ep[0], ep[1], sp[2])
        
def define_quad_line(sp, ep, n):
    '''
    n = surface_normal like (1,0,0) => x+ is normal
    '''
    if n == (0,0,-1):
        glVertex3f(sp[0], sp[1], sp[2])
        glVertex3f(sp[0], ep[1], sp[2])
        glVertex3f(sp[0], ep[1], sp[2])
        glVertex3f(ep[0], ep[1], sp[2])
        glVertex3f(ep[0], ep[1], sp[2])
        glVertex3f(ep[0], sp[1], sp[2])
        glVertex3f(ep[0], sp[1], sp[2])
        glVertex3f(sp[0], sp[1], sp[2])
    elif n == (0,0,1):
        glVertex3f(sp[0], sp[1], ep[2])
        glVertex3f(sp[0], ep[1], ep[2])
        glVertex3f(sp[0], ep[1], ep[2])
        glVertex3f(ep[0], ep[1], ep[2])
        glVertex3f(ep[0], ep[1], ep[2])
        glVertex3f(ep[0], sp[1], ep[2])
        glVertex3f(ep[0], sp[1], ep[2])
        glVertex3f(sp[0], sp[1], ep[2])
    elif n == (-1,0,0):
        glVertex3f(sp[0], sp[1], sp[2])
        glVertex3f(sp[0], ep[1], sp[2])
        glVertex3f(sp[0], ep[1], sp[2])
        glVertex3f(sp[0], ep[1], ep[2])
        glVertex3f(sp[0], ep[1], ep[2])
        glVertex3f(sp[0], sp[1], ep[2])
        glVertex3f(sp[0], sp[1], ep[2])
        glVertex3f(sp[0], sp[1], sp[2])
    elif n == (1,0,0):
        glVertex3f(ep[0], ep[1], sp[2])
        glVertex3f(ep[0], sp[1], sp[2])
        glVertex3f(ep[0], sp[1], sp[2])
        glVertex3f(ep[0], sp[1], ep[2])
        glVertex3f(ep[0], sp[1], ep[2])
        glVertex3f(ep[0], ep[1], ep[2])
        glVertex3f(ep[0], ep[1], ep[2])
        glVertex3f(ep[0], ep[1], sp[2])
    elif n == (0,-1,0):
        glVertex3f(sp[0], sp[1], sp[2])
        glVertex3f(ep[0], sp[1], sp[2])
        glVertex3f(ep[0], sp[1], sp[2])
        glVertex3f(ep[0], sp[1], ep[2])
        glVertex3f(ep[0], sp[1], ep[2])
        glVertex3f(sp[0], sp[1], ep[2])
        glVertex3f(sp[0], sp[1], ep[2])
        glVertex3f(sp[0], sp[1], sp[2])
    elif n == (0,1,0):
        glVertex3f(sp[0], ep[1], sp[2])
        glVertex3f(sp[0], ep[1], ep[2])
        glVertex3f(sp[0], ep[1], ep[2])
        glVertex3f(ep[0], ep[1], ep[2])
        glVertex3f(ep[0], ep[1], ep[2])
        glVertex3f(ep[0], ep[1], sp[2])
        glVertex3f(ep[0], ep[1], sp[2])
        glVertex3f(sp[0], ep[1], sp[2])