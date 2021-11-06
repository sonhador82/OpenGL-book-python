from .basic import Basic
from OpenGL.GL import *


class Point(Basic):
    def __init__(self, properties={}):
        super().__init__()

        # render verts as points
        self.settings["drawStyle"] = GL_POINT
        self.settings["pointSize"] = 8
        self.settings["roundedPoints"] = False
        self.setProperties(properties)

    def updateRenderSettings(self):
        glPointSize(self.settings["pointSize"])
        if self.settings["roundedPoints"]:
            glEnable(GL_POINT_SMOOTH)
        else:
            glDisable(GL_POINT_SMOOTH)
