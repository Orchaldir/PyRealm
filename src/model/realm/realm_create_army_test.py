import unittest


from model.map.province import Province
from model.realm.realm import Realm


class RealmCreateArmyTest(unittest.TestCase):

    def test_create_army(self):
        realm = Realm()        
        province = Province(None, 0,0)
        realm.add_province(province)
        
        army0 = realm.create_army(province, 1)
        self.assertNotEqual(army0, None)
        self.assertEqual(army0.realm, realm)
        self.assertEqual(army0.size, 1)
        self.assertEqual(army0.province, province)
        self.assertEqual(len(province.armies), 1)
        self.assertTrue(army0 in province.armies)
        self.assertEqual(len(realm.armies), 1)
        self.assertTrue(army0 in realm.armies)
        
        army1 = realm.create_army(province, 10)
        self.assertNotEqual(army1, None)
        self.assertEqual(army1.realm, realm)
        self.assertEqual(army1.size, 10)
        self.assertEqual(army1.province, province)
        self.assertEqual(len(province.armies), 2)
        self.assertTrue(army0 in province.armies)
        self.assertTrue(army1 in province.armies)
        self.assertEqual(len(realm.armies), 2)
        self.assertTrue(army0 in realm.armies)
        self.assertTrue(army1 in realm.armies)
    
    def test_invalid_province(self):    
        realm = Realm()        
        province = Province(None, 0,0)
        
        army0 = realm.create_army(province, 1)
        self.assertEqual(army0, None)
        self.assertEqual(len(province.armies), 0)
        self.assertEqual(len(realm.armies), 0)
        
        self.assertRaises(AssertionError, realm.create_army, None, 1)
        self.assertEqual(len(province.armies), 0)
        self.assertEqual(len(realm.armies), 0)
    
    def test_invalid_size(self):    
        realm = Realm()        
        province = Province(None, 0,0)
        realm.add_province(province)
        
        self.assertRaises(AssertionError, realm.create_army, province, 0)
        self.assertRaises(AssertionError, realm.create_army, province, -1)
        self.assertRaises(AssertionError, realm.create_army, province, None)
        
        
        self.assertEqual(len(province.armies), 0)
        self.assertEqual(len(realm.armies), 0)


def get_tests():
    return unittest.makeSuite(RealmCreateArmyTest, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())        
