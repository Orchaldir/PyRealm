from model.army.army import Army
from model.army.battle import Battle
from model.realm.realm import Realm
from utility.color import Color


class Result:

    def __init__(self):
        self.battles = []


class World:

    def __init__(self, map=None):
        self.armies = []
        self.realms = []
        self.next_army_id = 0
        self.next_realm_id = 0
        self.turn = 0
        self.map = map
    
    def create_army(self, realm):
        assert realm, 'Invalid realm!'
        
        if realm not in self.realms:
            return None
        
        army = Army(self.next_army_id, realm)   
        self.next_army_id += 1 
        self.armies.append(army)
        realm.armies.append(army)
        
        return army
        
    def create_realm(self, name, r, g, b):
        realm = Realm(self.next_realm_id, name, Color(r, g, b))
        self.next_realm_id += 1
        self.realms.append(realm)
        
        return realm
    
    def get_realm(self, index):
        if 0 <= index < len(self.realms):
            return self.realms[index]
        
        return None
    
    def tick(self):
        self.turn += 1
        result = Result()
        
        for realm in self.realms:
            for army in realm.armies:
                if army.action:
                    army.action.execute()
                    army.action = None
            
            for province in realm.provinces:
                if province.action:
                    province.action.execute()
                    province.action = None
        
        if self.map:
            for province in self.map.provinces.itervalues():
                realms = []
                
                for army in province.armies:
                    if army.realm not in realms:
                        realms.append(army.realm)
                
                if len(realms) > 1:
                    battle = Battle(province.armies[0], province.armies[1])
                    result.battles.append(battle)
        
        return result
