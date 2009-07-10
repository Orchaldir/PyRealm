import unittest


from model.realm.realm import Realm
from model.world import World


class WorldCreateArmyTest(unittest.TestCase):

    def test_create_army(self):
        world = World()
        
        realm = world.create_realm('Realm0', 0.1, 0.2, 0.3)
        
        army = world.create_army(realm)
        self.assertNotEqual(army, None)
        self.assertEqual(army.realm, realm)
        self.assertEqual(army.size, 0)
        self.assertEqual(army.province, None)
        self.assertEqual(len(world.armies), 1)
        self.assertTrue(army in world.armies)
        self.assertEqual(len(realm.armies), 1)
        self.assertTrue(army in realm.armies)
    
    def test_invalid_realm(self):
        world = World()
        
        self.assertRaises(AssertionError, world.create_army, None)
        
        realm = Realm()  
        
        army = world.create_army(realm)
        self.assertEqual(army, None)


def get_tests():
    return unittest.makeSuite(WorldCreateArmyTest, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())        
