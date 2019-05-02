from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Edge(object):
    def __init__(self, x1, y1, z1, x2, y2, z2, visible = False):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2
        self.visible = visible

    def Draw(self):
        if(self.visible):
            glVertex3f(self.x1, self.y1, self.z1) # 1 1 -1 -  0
            glVertex3f(self.x2, self.y2, self.z2) # -1 1 -1 - 1