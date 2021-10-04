from core.base import Base
from core.openGLUtils import OpenGLUtils
from OpenGL.GL import *


class Test(Base):
    def initialize(self):
        print("Init program")

        vsCode = """
        void main() {
            gl_Position = vec4(0.0, 0.0, 0.0, 1.0);
        }
        """

        fsCode = """
        out vec4 fragColor;
        void main() {
            fragColor = vec4(1.0, 1.0, 0.0, 1.0);
        }
        """

        # load and compile shaders
        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)

        # setup vertex array object
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        # render settings
        glPointSize(10)

    def update(self):
        # select progam to use when render
        glUseProgram(self.programRef)

        # renders geometrics via selected program
        glDrawArrays(GL_POINTS, 0, 1)


Test().run()

