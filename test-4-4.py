from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from geometry.sphere import SphereGeometry
from geometry.box import BoxGeometry
from material.surface import Surface
from material.material import Material


class Test(Base):
    def initialize(self):
        print("init app")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=640/480)
        self.camera.setPosition([0,0,7])

        geometry = SphereGeometry(radius=3)
        vsCode = """
        in vec3 vertexPosition;
        in vec3 vertexColor;
        out vec3 position;
        out vec3 color;
        uniform mat4 modelMatrix;
        uniform mat4 viewMatrix;
        uniform mat4 projectionMatrix;
        uniform float time;
        void main() {
            float offset = 0.2*sin(0.8*vertexPosition.x + time);
            vec3 pos = vertexPosition + vec3(0.0, offset, 0.0);
            gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(pos, 1);
            color = vertexColor;
        }
        """

        fsCode = """
        in vec3 position;
        in vec3 color;
        uniform float time;
        out vec4 fragColor;
        
        void main() {
            float r = abs(sin(time));
            vec4 c = vec4(r, -0.5*r, -0.5*r, 0.0);
            fragColor = vec4(color, 1.0) + c;
        }
        """

        material = Material(vsCode, fsCode)
        material.addUniform("float", "time", 0)
        material.locateUniforms()

        self.time = 0

        self.mesh2 = Mesh(BoxGeometry(), material)
        self.scene.add(self.mesh2)

    def update(self):
        self.time += 1 / 60
        self.mesh2.material.uniforms["time"].data = self.time
        #self.mesh2.rotateY(0.0514)
        #self.mesh2.rotateX(0.0337)
        self.renderer.render(self.scene, self.camera)


Test(screenSize=[640, 480]).run()
