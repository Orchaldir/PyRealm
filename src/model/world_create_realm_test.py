import unittest


from model.world import World


class WorldCreateRealmTest(unittest.TestCase):

    def test_create_realm(self):
        world = World()
        
        realm0 = world.create_realm('Realm0', 0.1, 0.2, 0.3)
        self.assertNotEqual(realm0, None)
        self.assertEqual(realm0.id, 0)
        self.assertEqual(realm0.name, 'Realm0')
        self.assertEqual(realm0.color.get_r(), 0.1)
        self.assertEqual(realm0.color.get_g(), 0.2)
        self.assertEqual(realm0.color.get_b(), 0.3)
        self.assertEqual(len(world.realms), 1)
        self.assertTrue(realm0 in world.realms)
        
        realm1 = world.create_realm('Realm1', 0.3, 0.2, 0.1)
        self.assertNotEqual(realm1, None)
        self.assertEqual(realm1.id, 1)
        self.assertEqual(realm1.name, 'Realm1')
        self.assertEqual(realm1.color.get_r(), 0.3)
        self.assertEqual(realm1.color.get_g(), 0.2)
        self.assertEqual(realm1.color.get_b(), 0.1)
        self.assertEqual(len(world.realms), 2)
        self.assertTrue(realm1 in world.realms)


def get_tests():
    return unittest.makeSuite(WorldCreateRealmTest, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())        
