

class Time:

    def __init__(self):
        self.turn = 0
        self.realms = []
    
    def add_realm(self, realm):
        self.realms.append(realm)
    
    def tick(self):
        self.turn += 1
        
        for realm in self.realms:
            for army in realm.armies:
                if army.action:
                    army.action.execute()
                    army.action = None
            
            for province in realm.provinces:
                if province.action:
                    province.action.execute()
                    province.action = None
