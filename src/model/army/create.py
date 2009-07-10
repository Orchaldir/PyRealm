

def can_create_army(realm, province, size):
    assert realm, 'Invalid realm!'
    assert province, 'Invalid province!'
    assert size > 0, 'Invalid size!'
    
    if province not in realm.provinces:
        return False
    
    return True


class CreateArmy:

    def __init__(self, world, realm, province, size):
        self.world = world
        self.realm = realm
        self.province = province
        self.size = size
        self.army = None
    
    def execute(self):
        self.army = self.world.create_army(self.realm)
        self.army.size = self.size
        self.province.add_army(self.army)
        
