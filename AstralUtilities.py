class vec2:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        self.t = (self.x, self.y)

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return vec2(self.x + other, self.y + other)
        else:
            return vec2(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return vec2(self.x * other, self.y * other)
        else:
            return vec2(self.x * other.x, self.y * other.y)

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            return vec2(self.x - other, self.y - other)
        else:
            return vec2(self.x - other.x, self.y - other.y)


class vec3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.t = (self.x, self.y, self.z)

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return vec2(self.x + other, self.y + other, self.z + other)
        else:
            return vec2(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return vec2(self.x * other, self.y * other, self.z * other)
        else:
            return vec2(self.x * other.x, self.y * other.y, self.z * other.z)

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            return vec2(self.x - other, self.y - other, self.z - other)
        else:
            return vec2(self.x - other.x, self.y - other.y, self.z - other.z)


class SpriteAnimation:
    def __init__(self, name, fps, anims):
        self.name = name
        self.fps = fps
        self.index = 0
        self.anims = anims
