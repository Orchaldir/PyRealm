import pyglet


class MapView:

    def __init__(self, map, length, space):
        self.map = map
        self.length = length
        self.altitude = 0.866 * length
        self.half = length / 2.0
        self.space = space
        
        total_width = (2 * self.map.width + 1) * self.altitude + (self.map.width - 1) * self.space        
        
        start_x = -self.length * (self.map.width - 1)
        start_y = -self.altitude * (self.map.height - 1) / 2.0
        
        self.start_x = [start_x, start_x + self.altitude]
        
        self.pos_x = []
        
        for i in range(0, self.map.width):
            self.pos_x.append((2.0 * self.altitude + self.space) * i)
        
        self.pos_y = []
        
        for i in range(0, self.map.height):
            self.pos_y.append(start_y + (1.5 * self.length + self.space) * i)
        
        self.batch = pyglet.graphics.Batch()
        
        for y in range(0, self.map.height):
            for x in range(0, self.map.width):
                province = self.map.get_province(x, y)
                self.add_province(province, self.start_x[y % 2] + self.pos_x[x], self.pos_y[y])
    
    def add_province(self, province, x, y):
        self.batch.add_indexed(7, pyglet.gl.GL_TRIANGLES, None, 
            [
                1, 0, 2,
                2, 0, 3,
                3, 0, 4,
                4, 0, 5,
                5, 0, 6,
                6, 0, 1],
            ('v2f', (
                x, y,
                x, y + self.length,
                x + self.altitude, y + self.half,
                x + self.altitude, y - self.half,
                x, y - self.length,
                x - self.altitude, y - self.half,
                x - self.altitude, y + self.half)))
    
    def draw(self):
        self.batch.draw()
        
        
        
        
        
            
