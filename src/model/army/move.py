

def can_move_army(army, province):
    assert army, 'Invalid army!'
    assert province, 'Invalid province!'    
    
    if not army.province:
        return False
        
    return army.province.is_neighbour(province)


class MoveArmy:

    def __init__(self, army, province):
        self.army = army
        self.province = province
    
    def execute(self):
        self.army.province.remove_army(self.army)
        self.province.add_army(self.army)   
