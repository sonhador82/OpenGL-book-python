from OpenGL.GL import *

from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute

class Test(Base):
    def initialize(self):
        print("init program")

        vsCode = """
        in vec3 position;
        void main() {
            gl_Position = vec4 (position.x, position.y, position.z, 1.0);
        }
        """

        fsCode = """
        out vec4 fragColor;
        void main() {
            fragColor = vec4(1.0, 1.0, 0.0, 1.0);
        }
        """

        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)

        ## render settings
        glLineWidth(4)

        ## setup vertex array
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        ## setup vertex attributes
        positionData = (
            (0.8, 0.0, 0.0),
            (0.4, 0.6, 0.0),
            (-0.4, 0.6, 0.0),
            (-0.8, 0.0, 0.0),
            (-0.4, -0.6, 0.0),
            (0.4, -0.6, 0.0)
        )
        self.vertexCount = len(positionData)
        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programRef, "position")

    def update(self):
        glUseProgram(self.programRef)
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.vertexCount)

Test().run()
