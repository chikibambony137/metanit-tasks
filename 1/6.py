class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

vec1 = Vector(1, 2)
vec2 = Vector(3, 4)

vec3 = vec1 + vec2
print(vec3.x, vec3.y)

vec4 = vec1 - vec2
print(vec4.x, vec4.y)
