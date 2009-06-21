import pyglet


from matrix import get_rotation


class MapView:

    def __init__(self, map, length, space):
        self.map = map
        self.length = length
        self.altitude = 0.866 * length
        self.half = length / 2.0
        self.space = space
        self.border = 10.0
        
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
        
        self.provinces_group = pyglet.graphics.OrderedGroup(0)
        self.border_group = pyglet.graphics.OrderedGroup(1)
        
        self.create_batch()
    
    def create_batch(self):
        self.batch = pyglet.graphics.Batch()
        
        for y in range(0, self.map.height):
            for x in range(0, self.map.width):
                province = self.map.get_province(x, y)
                pos_x = self.start_x[y % 2] + self.pos_x[x]
                pos_y = self.pos_y[y]
                
                self.add_province(province.terrain, pos_x, pos_y)
                
                if province.realm is not None:
                    for i in range(6):
                        neighbour = province.get_neighbour(i)
                        
                        if neighbour is None or neighbour.realm is not province.realm:
                            self.add_border(province.realm, pos_x, pos_y, i)                    
    
    def add_border(self, realm, x, y, direction):
        rotation = get_rotation(60.0 * direction)    
        
        x0, y0 = rotation.transform(self.altitude, -self.half)
        x1, y1 = rotation.transform(self.altitude,  self.half)
        x2, y2 = rotation.transform(self.altitude - self.border,  (self.half + self.border * self.half / self.altitude))
        x3, y3 = rotation.transform(self.altitude - self.border, -(self.half + self.border * self.half / self.altitude))
        
        self.batch.add_indexed(4, pyglet.gl.GL_TRIANGLES, self.border_group, 
            [
                0, 1, 2,
                0, 2, 3],
            ('v2f', (
                x + x0, y + y0,
                x + x1, y + y1,
                x + x2, y + y2,
                x + x3, y + y3)),
            ('c3B', (
                realm.r, realm.g, realm.b,
                realm.r, realm.g, realm.b,
                realm.r, realm.g, realm.b,
                realm.r, realm.g, realm.b)))
    
    def add_province(self, terrain, x, y):
        self.batch.add_indexed(7, pyglet.gl.GL_TRIANGLES, self.provinces_group, 
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
                x - self.altitude, y + self.half)),
            ('c3B', (
                terrain.r, terrain.g, terrain.b,
                terrain.r, terrain.g, terrain.b,
                terrain.r, terrain.g, terrain.b,
                terrain.r, terrain.g, terrain.b,
                terrain.r, terrain.g, terrain.b,
                terrain.r, terrain.g, terrain.b,
                terrain.r, terrain.g, terrain.b)))
    
    def draw(self):
        self.batch.draw()
        
        
        
        
        
            
