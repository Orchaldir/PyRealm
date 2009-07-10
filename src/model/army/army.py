

class Army:

    def __init__(self, id=0, realm=None):
        self.id = id
        self.realm = realm
        self.size = 0
        self.province = None
        self.action = None
    
    def remove(self):
        if self.province:
            self.province.remove_army(self)
