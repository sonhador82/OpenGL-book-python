from core.object3D import Object3D
from OpenGL.GL import *


class Mesh(Object3D):
    def __init__(self, geometry, material):
        super().__init__()

        self.geometry = geometry
        self.material = material

        # should be rendered
        self.visible = True

        # setup assotiations between attrs in geom and shader
        self.vaoRef = glGenVertexArrays(1)
        glBindVertexArray(self.vaoRef)
        for variableName, attributeObject in geometry.attributes.items():
            attributeObject.associateVariable(material.programRef, variableName)
        # unbind this vertex array object
        glBindVertexArray(0)
