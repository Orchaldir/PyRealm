

class Army:

    def __init__(self, realm, size=0):
        self.realm = realm
        self.size = size
        self.province = None
        self.action = None
    
    def remove(self):
        if self.province:
            self.province.remove_army(self)
