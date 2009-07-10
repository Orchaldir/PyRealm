import unittest


from model.realm.realm import Realm
from model.world import World


class WorldCreateArmyTest(unittest.TestCase):

    def test_create_army(self):
        world = World()
        
        realm = world.create_realm('Realm0', 0.1, 0.2, 0.3)
        
        army0 = world.create_army(realm)
        self.assertNotEqual(army0, None)
        self.assertEqual(army0.id, 0)
        self.assertEqual(army0.realm, realm)
        self.assertEqual(army0.size, 0)
        self.assertEqual(army0.province, None)
        self.assertEqual(len(world.armies), 1)
        self.assertTrue(army0 in world.armies)
        self.assertEqual(len(realm.armies), 1)
        self.assertTrue(army0 in realm.armies)
        
        army1 = world.create_army(realm)
        self.assertNotEqual(army1, None)
        self.assertEqual(army1.id, 1)
        self.assertEqual(army1.realm, realm)
        self.assertEqual(army1.size, 0)
        self.assertEqual(army1.province, None)
        self.assertEqual(len(world.armies), 2)
        self.assertTrue(army1 in world.armies)
        self.assertEqual(len(realm.armies), 2)
        self.assertTrue(army1 in realm.armies)
    
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
