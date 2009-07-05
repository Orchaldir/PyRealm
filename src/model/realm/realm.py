from model.army.army import Army


class Realm:

    def __init__(self, r=1.0, g=1.0, b=1.0):
        self.r = r
        self.g = g
        self.b = b
        self.armies = []
        self.provinces = []
    
    def add_province(self, province):
        assert province, 'Invalid province!'
        
        if province.realm:
            return False
        
        if province in self.provinces:
            return False
        
        self.provinces.append(province)
        province.realm = self
        
        return True
    
    def create_army(self, province, size):
        assert province, 'Invalid province!'
        assert size > 0, 'Invalid size!'
        
        if province not in self.provinces:
            return None
        
        army = Army(self, size)    
        self.armies.append(army)
        province.add_army(army)
        
        return army
    
    def remove_province(self, province):
        assert province, 'Invalid province!'
        
        if province not in self.provinces:
            return False
        
        self.provinces.remove(province)
        province.realm = None
            
        return True
            
