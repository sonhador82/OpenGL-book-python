from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from geometry.box import BoxGeometry
from geometry.polygon import PolygonGeometry
from geometry.sphere import SphereGeometry
from geometry.plane import PlaneGeometry
from material.surface import Surface


class Test(Base):
    def initialize(self):
        print("init app")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=640/480)
        self.camera.setPosition([0,0,4])

        geometry = BoxGeometry()
        material = Surface({"useVertexColors": True, "wireframe": True, "doubleSide": True})
        self.mesh = Mesh(geometry, material)
        self.scene.add(self.mesh)

        g2 = SphereGeometry()
        self.poly = Mesh(g2, material)
        self.scene.add(self.poly)

    def update(self):

        self.mesh.rotateY(0.0514)
        self.mesh.rotateX(0.0337)
        self.renderer.render(self.scene, self.camera)


Test(screenSize=[640, 480]).run()
