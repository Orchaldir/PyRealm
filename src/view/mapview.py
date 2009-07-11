import pyglet
import math


from utility.matrix import get_rotation


class MapView:

    def __init__(self, map, length, space, border, army):
        self.map = map
        self.length = length
        self.altitude = 0.866 * length
        self.half = length / 2.0
        self.space = space
        self.border = border
        self.army = army
        
        start_x = self.altitude + self.space
        start_y = self.length + self.space
        
        self.start_x = [start_x, start_x + self.altitude]
        
        self.pos_x = []
        
        for i in range(0, self.map.width):
            self.pos_x.append((2.0 * self.altitude + self.space) * i)
        
        self.pos_y = []
        
        for i in range(0, self.map.height):
            self.pos_y.append(start_y + (1.5 * self.length + self.space) * i)
        
        self.provinces_group = pyglet.graphics.OrderedGroup(0)
        self.realm_group = pyglet.graphics.OrderedGroup(1)
        
        self.create_batch()
    
    def create_batch(self):
        self.batch = pyglet.graphics.Batch()
        
        for province in self.map.provinces.itervalues():
            pos_x, pos_y = self.get_position(province.x, province.y)
            
            self.create_province(province.terrain, pos_x, pos_y)
            
            if province.armies:
                i = 0
                degrees = 360.0 / len(province.armies)
                for army in province.armies:
                    self.create_army(army, pos_x, pos_y, i * degrees)
                    i += 1
            
            if province.realm:
                for i in range(6):
                    neighbour = province.get_neighbour(i)
                    
                    if not neighbour or neighbour.realm is not province.realm:
                        self.create_border(province.realm, pos_x, pos_y, i)  
    
    def create_army(self, army, x, y, degrees):
        rotation = get_rotation(degrees)   
        
        x0, y0 = rotation.transform((self.altitude + self.army) / 2.0, -self.army / 2.0)
        x1, y1 = rotation.transform((self.altitude + self.army) / 2.0,  self.army / 2.0)
        x2, y2 = rotation.transform((self.altitude - self.army) / 2.0,  self.army / 2.0)
        x3, y3 = rotation.transform((self.altitude - self.army) / 2.0, -self.army / 2.0)
        
        r = army.realm.color.get_int_r()
        g = army.realm.color.get_int_g()
        b = army.realm.color.get_int_b()
        
        self.batch.add_indexed(4, pyglet.gl.GL_TRIANGLES, self.realm_group, 
            [
                0, 1, 2,
                0, 2, 3],
            ('v2f', (
                x + x0, y + y0,
                x + x1, y + y1,
                x + x2, y + y2,
                x + x3, y + y3)),
            ('c3B', (
                r, g, b,
                r, g, b,
                r, g, b,
                r, g, b)))                 
    
    def create_border(self, realm, x, y, direction):
        rotation = get_rotation(60.0 * direction)    
        
        x0, y0 = rotation.transform(self.altitude, -self.half)
        x1, y1 = rotation.transform(self.altitude,  self.half)
        x2, y2 = rotation.transform(self.altitude - self.border,  (self.half + self.border * self.half / self.altitude))
        x3, y3 = rotation.transform(self.altitude - self.border, -(self.half + self.border * self.half / self.altitude))
        
        r = realm.color.get_int_r()
        g = realm.color.get_int_g()
        b = realm.color.get_int_b()
        
        self.batch.add_indexed(4, pyglet.gl.GL_TRIANGLES, self.realm_group, 
            [
                0, 1, 2,
                0, 2, 3],
            ('v2f', (
                x + x0, y + y0,
                x + x1, y + y1,
                x + x2, y + y2,
                x + x3, y + y3)),
            ('c3B', (
                r, g, b,
                r, g, b,
                r, g, b,
                r, g, b)))
    
    def create_province(self, terrain, x, y):
        r = terrain.color.get_int_r()
        g = terrain.color.get_int_g()
        b = terrain.color.get_int_b()
        
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
                r, g, b,
                r, g, b,
                r, g, b,
                r, g, b,
                r, g, b,
                r, g, b,
                r, g, b)))                
    
    def draw(self):
        self.batch.draw()
    
    def get_province(self, mouse_x, mouse_y):
        radius = self.altitude**2
    
        for y in range(0, self.map.height):
            for x in range(0, self.map.width):
                pos_x, pos_y = self.get_position(x, y)
                
                dx = mouse_x - pos_x
                dy = mouse_y - pos_y
                
                distance = dx**2 + dy**2
                
                if distance >= radius:
                    continue
                    
                province = self.map.get_province(x, y)    
                
                if not province.armies:
                    return province
                
                i = 0
                degrees = 360.0 / len(province.armies)
                
                for army in province.armies:
                    if self.get_army(dx, dy, i * degrees):
                        return army
                    i += 1                
                
                return province
            
        return None
    
    def get_army(self, x, y, degrees):
        rotation = get_rotation(degrees)   
        
        cx, cy = rotation.transform(self.altitude / 2.0, 0.0)
        distance = (x - cx)**2 + (y -cy)**2
        
        return distance < math.sqrt(2.0 * self.army**2)
    
    def get_position(self, x, y):
        return self.start_x[y % 2] + self.pos_x[x], self.pos_y[y]
        
        
        
        
        
            
