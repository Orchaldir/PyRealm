

def can_create_province(realm, army):
    assert realm, 'Invalid realm!'
    assert army, 'Invalid army!'
    assert army.province, 'Invalid province!'
    
    if realm is not army.realm:
        return False
    
    if army.province.realm:
        return False
    
    return True


class CreateProvince:

    def __init__(self, realm, army):
        self.realm = realm
        self.army = army
    
    def execute(self):
        self.army.realm.add_province(self.army.province)
