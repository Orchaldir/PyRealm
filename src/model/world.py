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
        self.turn = 0
        self.map = map
    
    def create_army(self, realm):
        assert realm, 'Invalid realm!'
        
        if realm not in self.realms:
            return None
        
        army = Army(realm, 0)    
        self.armies.append(army)
        realm.armies.append(army)
        
        return army
        
    def create_realm(self, name, r, g, b):
        realm = Realm(name, Color(r, g, b))
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
                        realms.append(army)
                
                if len(realms) > 1:
                    battle = Battle(province.armies[0], province.armies[1])
                    result.battles.append(battle)
        
        return result
