from model.realm.realm import Realm


class World:

    def __init__(self):
        self.realms = []
        self.turn = 0
    
    def create_realm(self, name, r, g, b):
        realm = Realm(name, r, g, b)
        self.realms.append(realm)
        
        return realm
    
    def get_realm(self, index):
        if 0 <= index < len(self.realms):
            return self.realms[index]
        
        return None
    
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
