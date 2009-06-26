import unittest


from model.map.province import Province
from model.realm.realm import Realm


class RealmAddProvinceTest(unittest.TestCase):

    def test_add_province(self):
        realm = Realm()
        
        province = Province(None, 0,0)
        self.assertTrue(realm.add_province(province))
        self.assertEqual(len(realm.provinces), 1)
        self.assertEqual(province.realm, realm)
        self.assertTrue(province in realm.provinces)
        
        province = Province(None, 1,0)
        self.assertTrue(realm.add_province(province))
        self.assertEqual(len(realm.provinces), 2)
        self.assertEqual(province.realm, realm)
        self.assertTrue(province in realm.provinces)
    
    def test_second_time(self):    
        realm = Realm()
        
        province = Province(None, 0,0)
        self.assertTrue(realm.add_province(province))    
        self.assertFalse(realm.add_province(province))
        self.assertTrue(province in realm.provinces)
        self.assertEqual(province.realm, realm)
        self.assertEqual(len(realm.provinces), 1)
    
    def test_invalid_province(self):    
        realm = Realm()
        
        self.assertRaises(AssertionError, realm.add_province, None)


def get_tests():
    return unittest.makeSuite(RealmAddProvinceTest, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())        
