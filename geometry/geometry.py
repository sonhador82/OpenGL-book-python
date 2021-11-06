from core.attribute import Attribute


class Geometry:
    def __init__(self):
        # Store attribute objects indexed by name os associated variable in shader
        # shader variable associations setup later
        # and stored in vertex array object in Mesh
        self.attributes = {}
        # number of verts
        self.vertexCount = None

    def addAttribute(self, dataType, variableName, data):
        self.attributes[variableName] = Attribute(dataType, data)

    def countVertices(self):
        # number of vertices may be calculated from length of
        # any Attribute object's array of data
        attrib = list(self.attributes.values())[0]
        self.vertexCount = len(attrib.data)
