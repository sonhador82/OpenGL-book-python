from OpenGL.GL import *
import numpy

class Attribute:
    def __init__(self, dataType, data):
        # type of elemetns in data array
        # int | float | vec2 | vec3 | vec4
        self.dataType = dataType

        # array of data in buffer
        self.data = data

        # ref for avaiable GPU buffer
        self.bufferRef = glGenBuffers(1)

        # upload data immediately
        self.uploadData()

    # upload data to GPU buffer
    def uploadData(self):
        # convert data to numpy array format
        # convert numbers to 32 bit floats
        data = numpy.array(self.data).astype(numpy.float32)

        # select buffer
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)

        # store data in currently bound buffer
        glBufferData(GL_ARRAY_BUFFER, data.ravel(), GL_STATIC_DRAW)

    def associateVariable(self, programRef, variableName):
        # get ref for program variable with given name
        variableRef = glGetAttribLocation(programRef, variableName)

        # if the program does not reference the variable - exit
        if variableRef == -1:
            return

        # select buffer used by the following functions
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)

        # how data will be read
        if self.dataType == "int":
            glVertexAttribPointer(variableRef, 1, GL_INT, False, 0, None)
        elif self.dataType == "float":
            glVertexAttribPointer(variableRef, 1, GL_FLOAT, False, 0, None)
        elif self.dataType == "vec2":
            glVertexAttribPointer(variableRef, 2, GL_FLOAT, False, 0, None)
        elif self.dataType == "vec3":
            glVertexAttribPointer(variableRef, 3, GL_FLOAT, False, 0, None)
        elif self.dataType == "vec4":
            glVertexAttribPointer(variableRef, 4, GL_FLOAT, False, 0, None)
        else:
            raise Exception(f"Attribue {variableName} has unknown type {self.dataType}")
        glEnableVertexAttribArray(variableRef)
