

def can_move_army(realm, army, province):
    assert realm, 'Invalid realm!'
    assert army, 'Invalid army!'
    assert province, 'Invalid province!'
    
    if realm is not army.realm:
        return False    
    
    if not army.province:
        return False
        
    return army.province.is_neighbour(province)


class MoveArmy:

    def __init__(self, realm, army, province):
        self.realm = realm
        self.army = army
        self.province = province
    
    def execute(self):
        self.army.province.remove_army(self.army)
        self.province.add_army(self.army)   
