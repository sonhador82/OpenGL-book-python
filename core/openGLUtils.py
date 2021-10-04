from OpenGL.GL import *


class OpenGLUtils:
    @staticmethod
    def initializeShader(shaderCode, shaderType):
        shaderCode = '#version 330\n ' + shaderCode
        shaderRef = glCreateShader(shaderType)
        glShaderSource(shaderRef, shaderCode)
        glCompileShader(shaderRef)
        compileSuccess = glGetShaderiv(shaderRef, GL_COMPILE_STATUS)
        if not compileSuccess:
            errorMessage = glGetShaderInfoLog(shaderRef)
            glDeleteShader(shaderRef)
            errorMessage = '\n' + errorMessage.decode('utf-8')
            raise Exception(errorMessage)
        return shaderRef

    @staticmethod
    def initializeProgram(vertexShaderCode, fragmentShaderCode):
        vertexShaderRef = OpenGLUtils.initializeShader(vertexShaderCode, GL_VERTEX_SHADER)
        fragmentShaderRef = OpenGLUtils.initializeShader(fragmentShaderCode, GL_FRAGMENT_SHADER)

        # create empty program
        programRef = glCreateProgram()

        # attache shaders to program
        glAttachShader(programRef, vertexShaderRef)
        glAttachShader(programRef, fragmentShaderRef)

        # link vertex to fragment
        glLinkProgram(programRef)

        linkSuccess = glGetProgramiv(programRef, GL_LINK_STATUS)
        if not linkSuccess:
            errorMessage = glGetProgramInfoLog(programRef)
            # free mem used to store
            glDeleteProgram(programRef)

            errorMessage = '\n' + errorMessage.decode('utf-8')
            raise Exception(errorMessage)
        return programRef

    @staticmethod
    def printSystemInfo():
        print(f" Vendor: {glGetString(GL_VENDOR).decode('utf-8')}")
        print(f"Renderer: {glGetString(GL_RENDERER).decode('utf-8')}")
        print(f"OpenGL version supported: {glGetString(GL_VERSION).decode('utf-8')}")
        print(f" GLSL version supported: {glGetString(GL_SHADING_LANGUAGE_VERSION).decode('utf-8')} ")

