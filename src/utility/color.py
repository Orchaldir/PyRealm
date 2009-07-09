

class Color:

    def __init__(self, r, g, b, a=1.0):
        assert 0.0 <= r <= 1.0, 'Ivalid value!'
        assert 0.0 <= g <= 1.0, 'Ivalid value!'
        assert 0.0 <= b <= 1.0, 'Ivalid value!'
        assert 0.0 <= a <= 1.0, 'Ivalid value!'
        
        self.r = r
        self.g = g
        self.b = b
        self.a = a
    
    def get_r(self):
        return self.r
    
    def get_g(self):
        return self.g
    
    def get_b(self):
        return self.b
    
    def get_a(self):
        return self.a
    
    def get_int_r(self):
        return int(self.r * 255)
    
    def get_int_g(self):
        return int(self.g * 255)
    
    def get_int_b(self):
        return int(self.b * 255)
    
    def get_int_a(self):
        return int(self.a * 255)
