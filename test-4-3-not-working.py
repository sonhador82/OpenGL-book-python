from math import sin
from numpy import arange
from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from geometry.geometry import Geometry
from material.surface import Surface
from material.point import Point
from material.line import Line

class Test(Base):
    def initialize(self):
        print("init app")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=640/480)
        self.camera.setPosition([0,0,0.5])

        geometry = Geometry()
        posData = []
        for x in arange(-3.2, 3.2, 0.3):
            posData.append([x, sin(x), 0])
        breakpoint()
        geometry.addAttribute("vec3", "vertexPosition", posData)
        geometry.countVertices()

        pointMaterial = Point({"baseColor": [1,1,0], "pointSize": 10})
        pointMesh = Mesh(geometry, pointMaterial)

        self.scene.add(pointMesh)

        # material = Surface({"useVertexColors": True, "wireframe": True, "doubleSide": True})
        # self.mesh = Mesh(geometry, material)
        # self.scene.add(self.mesh)


    def update(self):
        self.renderer.render(self.scene, self.camera)


Test(screenSize=[640, 480]).run()
