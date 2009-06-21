import unittest


from model.map.map import Map
from model.realm.realm import Realm


class Realm_add_province_Test(unittest.TestCase):

    def test_add_province(self):
        test_map = Map()
        test_map.create(2, 4)        
        realm = Realm()
        
        province = test_map.get_province(0,0)
        self.assertTrue(realm.add_province(province))
        self.assertEqual(len(realm.provinces), 1)
        self.assertEqual(province.realm, realm)
        self.assertTrue(province in realm.provinces)
        
        province = test_map.get_province(1,0)
        self.assertTrue(realm.add_province(province))
        self.assertEqual(len(realm.provinces), 2)
        self.assertEqual(province.realm, realm)
        self.assertTrue(province in realm.provinces)
    
    def test_second_time(self):    
        test_map = Map()
        test_map.create(2, 4)        
        realm = Realm()
        
        province = test_map.get_province(0,0)
        self.assertTrue(realm.add_province(province))    
        self.assertFalse(realm.add_province(province))
        self.assertTrue(province in realm.provinces)
        self.assertEqual(province.realm, realm)
        self.assertEqual(len(realm.provinces), 1)
    
    def test_invalid_province(self):    
        realm = Realm()
        
        self.assertFalse(realm.add_province(None))


def get_tests():
    return unittest.makeSuite(Realm_add_province_Test, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())        
