

class Province:

    neighbours_x = [[1, 0, -1, -1, -1, 0], [1, 1,  0, -1,  0, 1]]
    neighbours_y = [0, 1, 1, 0, -1, -1]

    def __init__(self, map, x, y, terrain=None):
        self.map = map
        self.x = x
        self.y = y
        self.terrain = terrain
        self.realm = None
    
    def get_neighbour(self, direction):
        if direction not in range(6):
            return None
        
        x = self.x + Province.neighbours_x[self.y % 2][direction]
        y = self.y + Province.neighbours_y[direction]
        
        return self.map.get_province(x, y)
    
    def is_neighbour(self, province):
        if province is None or self.map is not province.map:
            return False
        
        row = self.y % 2
        
        for i in range(6):
            x = self.x + Province.neighbours_x[row][i]
            y = self.y + Province.neighbours_y[i]
            
            if x == province.x and y == province.y:
                return True
            
        return False
