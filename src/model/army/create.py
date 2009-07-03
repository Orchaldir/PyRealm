

def can_create_army(realm, province, size):
    assert realm, 'Invalid realm!'
    assert province, 'Invalid province!'
    assert size > 0, 'Invalid size!'
    
    if province not in realm.provinces:
        return False
    
    return True


class CreateArmy:

    def __init__(self, realm, province, size):
        self.realm = realm
        self.province = province
        self.size = size
        self.army = None
    
    def execute(self):
        self.army = self.realm.create_army(self.province, self.size)
