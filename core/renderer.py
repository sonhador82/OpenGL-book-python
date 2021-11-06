from OpenGL.GL import *
from core.mesh import Mesh


class Renderer:
    def __init__(self, clearColor=[0, 0, 0]):
        glEnable(GL_DEPTH_TEST)
        # req for antialias
        glEnable(GL_MULTISAMPLE)
        glClearColor(clearColor[0], clearColor[1], clearColor[2], 1)

    def render(self, scene, camera):
        # clear color and depth buffer
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # update camera view
        camera.updateViewMatrix()

        # extract list of all mesh object in scene
        descendantList = scene.getDescendantList()
        meshFilter = lambda x: isinstance(x, Mesh)
        meshList = list(filter(meshFilter, descendantList))

        for mesh in meshList:
            if not mesh.visible:
                continue
            glUseProgram(mesh.material.programRef) \
                # bind vao
            glBindVertexArray(mesh.vaoRef)
            # update uniforms stored outside of mat
            mesh.material.uniforms["modelMatrix"].data = mesh.getWorldMatrix()
            mesh.material.uniforms["viewMatrix"].data = camera.viewMatrix
            mesh.material.uniforms[
                "projectionMatrix"].data = camera.projectionMatrix
            # update uniforms stored in material
            for variableName, uniformObject in mesh.material.uniforms.items():
                uniformObject.uploadData()

            # update render settings
            mesh.material.updateRenderSettings()

            glDrawArrays(mesh.material.settings["drawStyle"], 0,
                         mesh.geometry.vertexCount)
            