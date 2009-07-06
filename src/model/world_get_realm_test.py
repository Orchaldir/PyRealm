import unittest


from model.world import World


class WorldGetRealmTest(unittest.TestCase):

    def test_get_realm(self):
        world = World()
        
        realm0 = world.create_realm('Realm0', 0.1, 0.2, 0.3)
        realm1 = world.create_realm('Realm1', 0.1, 0.2, 0.3)
        
        self.assertEqual(realm0, world.get_realm(0))
        self.assertEqual(realm1, world.get_realm(1))
    
    def test_invalid_index(self):
        world = World()
        
        realm0 = world.create_realm('Realm0', 0.1, 0.2, 0.3)
        realm1 = world.create_realm('Realm1', 0.1, 0.2, 0.3)
        
        self.assertEqual(None, world.get_realm(-1))
        self.assertEqual(None, world.get_realm(2))
        self.assertEqual(None, world.get_realm(None))


def get_tests():
    return unittest.makeSuite(WorldGetRealmTest, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())        
