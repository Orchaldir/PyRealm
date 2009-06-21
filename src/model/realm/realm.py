

class Realm:

    def __init__(self, r=255, g=255, b=255):
        self.r = r
        self.g = g
        self.b = b
        self.provinces = []
    
    def add_province(self, province):
        if province is None:
            return False
        
        if province.realm is not None:
            return False
        
        if province in self.provinces:
            return False
        
        self.provinces.append(province)
        province.realm = self
        
        return True
    
    def remove_province(self, province):
        if province is None:
            return False
        
        if province not in self.provinces:
            return False
        
        self.provinces.remove(province)
        province.realm = None
            
        return True
            