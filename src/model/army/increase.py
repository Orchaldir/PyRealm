

def can_increase_army(realm, army):
    assert realm, 'Invalid realm!'
    assert army, 'Invalid army!'
    
    if realm is not army.realm:
        return False
    
    return True


class IncreaseArmy:

    def __init__(self, realm, army):
        self.realm = realm
        self.army = army
    
    def execute(self):
        self.army.size += 1
