

def can_create_province(army):
    assert army, 'Invalid army!'
    assert army.province, 'Invalid province!'
    
    if army.province.realm:
        return False
    
    return True


class CreateProvince:

    def __init__(self, army):
        self.army = army
    
    def execute(self):
        self.army.realm.add_province(self.army.province)
