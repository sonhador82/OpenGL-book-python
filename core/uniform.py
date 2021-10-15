from OpenGL.GL import *


class Uniform:
    def __init__(self, dataType, data):
        # type int | bool | float | vec2,3,4
        self.dataType = dataType

        # data to be sent to uniform var
        self.data = data

        # ref for var location in programm
        self.variableRef = None

    # get and store ref for pogram var name with given name
    def locateVariable(self, programRef, variableName):
        self.variableRef = glGetUniformLocation(programRef, variableName)

    # store data in uniform varible previosly located
    def uploadData(self):
        if self.variableRef == -1:
            return
        if self.dataType == 'int':
            glUniform1i(self.variableRef, self.data)
        elif self.dataType == 'bool':
            glUniform1i(self.variableRef, self.data)
        elif self.dataType == 'float':
            glUniform1f(self.variableRef, self.data)
        elif self.dataType == 'vec2':
            glUniform2f(self.variableRef, self.data[0], self.data[1])
        elif self.dataType == 'vec3':
            glUniform3f(self.variableRef, self.data[0], self.data[1], self.data[2])
        elif self.dataType == 'vec4':
            glUniform4f(self.variableRef, self.data[0], self.data[1], self.data[2], self.data[3])
        elif self.dataType == 'mat4':
            glUniformMatrix4fv(self.variableRef, 1, GL_TRUE, self.data)
