import unittest


from model.world import World


class WorldCreateRealmTest(unittest.TestCase):

    def test_create_realm(self):
        world = World()
        
        realm = world.create_realm('Realm0', 0.1, 0.2, 0.3)
        self.assertNotEqual(realm, None)
        self.assertEqual(realm.name, 'Realm0')
        self.assertEqual(realm.color.get_r(), 0.1)
        self.assertEqual(realm.color.get_g(), 0.2)
        self.assertEqual(realm.color.get_b(), 0.3)
        self.assertEqual(len(world.realms), 1)
        self.assertTrue(realm in world.realms)


def get_tests():
    return unittest.makeSuite(WorldCreateRealmTest, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())        
