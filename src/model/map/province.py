

class Province:

    neighbours_x = [[1, 0, -1, -1, -1, 0], [1, 1,  0, -1,  0, 1]]
    neighbours_y = [0, 1, 1, 0, -1, -1]

    def __init__(self, map, x, y, terrain=None):
        self.map = map
        self.x = x
        self.y = y
        self.terrain = terrain
        self.realm = None
        self.armies = []
        self.action = None
    
    def add_army(self, army):
        assert army, 'Invalid army!'
        
        if army in self.armies:
            return False
        
        if army.province:
            return False
        
        self.armies.append(army)
        army.province = self
        
        return True
    
    def get_neighbour(self, direction):
        assert direction in range(6), '%s not a direction!' % (direction)
        
        x = self.x + Province.neighbours_x[self.y % 2][direction]
        y = self.y + Province.neighbours_y[direction]
        
        return self.map.get_province(x, y)
    
    def is_neighbour(self, province):
        assert province, 'Invalid province!'
        
        if self.map is not province.map:
            return False
        
        row = self.y % 2
        
        for i in range(6):
            x = self.x + Province.neighbours_x[row][i]
            y = self.y + Province.neighbours_y[i]
            
            if x == province.x and y == province.y:
                return True
            
        return False
    
    def remove_army(self, army):
        assert army, 'Invalid army!'
        
        if army not in self.armies:
            return False
        
        self.armies.remove(army)
        army.province = None
        
        return True
