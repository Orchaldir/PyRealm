from model.army.army import Army


class Realm:

    def __init__(self, id=0, name='Test', color=None):
        self.id = id
        self.name = name
        self.color = color
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
    
    def remove_province(self, province):
        assert province, 'Invalid province!'
        
        if province not in self.provinces:
            return False
        
        self.provinces.remove(province)
        province.realm = None
            
        return True
            
