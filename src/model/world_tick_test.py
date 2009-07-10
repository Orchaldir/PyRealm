import unittest


from model.army.army import Army
from model.map.map import Map
from model.map.province import Province
from model.realm.realm import Realm
from model.world import World


class Action:

    def __init__(self):
        self.count = 0
    
    def execute(self):
        self.count += 1 


class WorldTickTest(unittest.TestCase):

    def test_actions(self):
        world = World()
        realm = world.create_realm('Realm0', 1.0, 1.0, 1.0)
        province = Province(None, 0,0)
        action0 = Action()
        province.action = action0
        realm.add_province(province)
        
        result = world.tick()
        
        self.assertEqual(world.turn, 1)
        self.assertEqual(action0.count, 1)
        self.assertEqual(province.action, None)
        self.assertEqual(len(result.battles), 0)
        
        army = world.create_army(realm)
        army.size = 1
        province.add_army(army)
        
        action1 = Action()
        army.action = action1
        
        result = world.tick()
        
        self.assertEqual(world.turn, 2)
        self.assertEqual(action0.count, 1)
        self.assertEqual(action1.count, 1)
        self.assertEqual(army.action, None)
        self.assertEqual(province.action, None)
        self.assertEqual(len(result.battles), 0)
        
    def test_battles(self):
        map = Map()
        map.create(None, 3, 3)
        
        world = World(map)
        realm0 = world.create_realm('Realm0', 1.0, 1.0, 1.0)
        realm1 = world.create_realm('Realm1', 1.0, 1.0, 1.0)
        
        province = map.get_province(0, 0)
                
        army0 = Army(0, realm0)
        army0.size = 2
        army1 = Army(0, realm1)
        army1.size = 1
        
        province.add_army(army0)
        province.add_army(army1)
        
        result = world.tick()
        
        self.assertEqual(len(result.battles), 1)
        
        battle = result.battles[0]
        
        self.assertEqual(battle.army0, army0)
        self.assertEqual(battle.army1, army1)
        
        self.assertEqual(army0.size, 1)
        self.assertEqual(army1.size, 0)
        
        self.assertEqual(army0.province, province)
        self.assertTrue(army0 in province.armies)
        self.assertEqual(army1.province, None)
        self.assertFalse(army1 in province.armies)    


def get_tests():
    return unittest.makeSuite(WorldTickTest, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())          
        
