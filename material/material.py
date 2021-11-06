from core.openGLUtils import OpenGLUtils
from core.uniform import Uniform
from OpenGL.GL import *


class Material:
    def __init__(self, vertexShaderCode, fragmentShaderCode):
        self.programRef = OpenGLUtils.initializeProgram(vertexShaderCode, fragmentShaderCode)
        # store uniform objects, indexed by name of associated var in shader
        self.uniforms = {}

        # each shader typically contains these uniforms;
        # values will be set during render process from Mesh/Camera
        # additional uniforms added by extending casses
        self.uniforms["modelMatrix"] = Uniform("mat4", None)
        self.uniforms["viewMatrix"] = Uniform("mat4", None)
        self.uniforms["projectionMatrix"] = Uniform("mat4", None)

        # store opengl render settings indexed by var name
        self.settings = {}
        self.settings["drawStyle"] = GL_TRIANGLES

    def addUniform(self, dataType, variableName, data):
        self.uniforms[variableName] = Uniform(dataType, data)

    # init all unform vars refs
    def locateUniforms(self):
        for variableName, uniformObject in self.uniforms.items():
            uniformObject.locateVariable(self.programRef, variableName)

    # configure opegl with render settings
    def updateRenderSettings(self):
        pass

    ## convenience method for setting multiple material "properties"
    # (uniform and render setting values) from a dictionary
    def setProperties(self, properties):
        for name, data in properties.items():
            # update uniforms
            if name in self.uniforms.keys():
                self.uniforms[name].data = data
            # update render settings
            elif name in self.settings.keys():
                self.settings[name] = data
            # unknown prop type
            else:
                raise Exception(f"Material has no propertie named: {name}")
