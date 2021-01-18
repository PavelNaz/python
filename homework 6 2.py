class Road:
    _length = None
    _width = None
    _weight = None
    _thickness = None

    def __init__(self, length, width, weight, thickness):
        self._length = length
        self._width = width
        self._weight = weight
        self._thickness = thickness

    def calculate(self):
        return self._length * self._width * self._weight * self._thickness

road = Road (length=5000,width=50,weight=50,thickness=0.1)
print(road.calculate())