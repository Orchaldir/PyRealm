import unittest


from model.map.province import Province
from model.realm.realm import Realm
from model.world import World


class Action:

    def __init__(self):
        self.count = 0
    
    def execute(self):
        self.count += 1 


class WorldTickTest(unittest.TestCase):

    def test_tick(self):
        world = World()
        realm = world.create_realm('Realm0', 1.0, 1.0, 1.0)
        province = Province(None, 0,0)
        action0 = Action()
        province.action = action0
        realm.add_province(province)
        
        world.tick()
        
        self.assertEqual(world.turn, 1)
        self.assertEqual(action0.count, 1)
        self.assertEqual(province.action, None)
        
        army = realm.create_army(province, 1)
        action1 = Action()
        army.action = action1
        
        world.tick()
        
        self.assertEqual(world.turn, 2)
        self.assertEqual(action0.count, 1)
        self.assertEqual(action1.count, 1)
        self.assertEqual(army.action, None)
        self.assertEqual(province.action, None)
        
        


def get_tests():
    return unittest.makeSuite(WorldTickTest, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())          
        
