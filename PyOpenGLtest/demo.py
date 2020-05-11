#!/usr/bin/env python
# coding: utf-8

import cv2
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
import glfw
from matplotlib import pyplot as plt

import elements as el

def initGL(dw, dh):
# Initialize the library
    if not glfw.init():
        return
    # Set window hint NOT visible
    glfw.window_hint(glfw.VISIBLE, False)
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(dw, dh, "hidden window", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    print('Vendor :', glGetString(GL_VENDOR))
    print('GPU :', glGetString(GL_RENDERER))
    print('OpenGL version :', glGetString(GL_VERSION))

    # specify to use OpenGL4.0
#     glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
#     glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 0)
#     glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)    
    return window

def main():
    DISPLAY_WIDTH = 1000
    DISPLAY_HEIGHT = 1000

    camera_pos = (10, -10, 20)
    draw_axis = (100, 1) # area, step
    cube_size = 5
    axis_size = 5
    
    window = initGL(DISPLAY_WIDTH, DISPLAY_HEIGHT)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
#     glEnable(GL_CULL_FACE)
#     glCullFace(GL_BACK)
        
    light_ambient = [1., 1., 1.]
    light_position = [1, -5, -5, 2]
    
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    
    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    near = 0.01
    far = 1000
    gluPerspective(45, (DISPLAY_WIDTH / DISPLAY_HEIGHT), 0.1, 100)

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)     # 環境光
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)   # 光源の位置

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(30, -30, 50,
              0, 0, 0,
              0, 0, 1)

    el.axis.draw_axes(axis_size)
    el.grid.draw_grid(*draw_axis)
    el.cube.draw_cube(cube_size)
    el.cube.draw_cube_wire(cube_size)
    
    image_buffer = glReadPixels(0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT, OpenGL.GL.GL_RGB, OpenGL.GL.GL_UNSIGNED_BYTE)
    image = np.frombuffer(image_buffer, dtype=np.uint8).reshape(DISPLAY_WIDTH, DISPLAY_HEIGHT, 3)
    
    glfw.destroy_window(window)
    glfw.terminate()
    image = np.flip(image, 0)
    
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imwrite("image.png", image)
    

if __name__ == "__main__":
    main()