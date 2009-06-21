import math

class Matrix:

    def __init__(self, m00=1.0, m10=0.0, m01=0.0, m11=1.0):
        self.m00 = m00
        self.m10 = m10
        self.m01 = m01
        self.m11 = m11
    
    def transform(self, x, y):
        return self.m00 * x + self.m10 * y, self.m01 * x + self.m11 * y


def get_rotation(degrees):
    sin = math.sin(math.radians(degrees))
    cos = math.cos(math.radians(degrees))
    
    return Matrix(cos, -sin, sin, cos)
