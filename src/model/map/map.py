from model.map.province import Province

class Map:

    def __init__(self):
        self.width = 0
        self.height = 0
        self.provinces = {}
    
    def create(self, terrain, width, height):
        self.width = width
        self.height = height
        
        for x in range(0, width):
            for y in range(0, height):
                self.provinces[self.get_index(x, y)] = Province(self, x, y, terrain)
                
    
    def get_province(self, x, y):
        index = self.get_index(x, y)
        
        if index in self.provinces:
            return self.provinces[index]
        
        return None
    
    def get_index(self, x, y):
        return (x, y)
