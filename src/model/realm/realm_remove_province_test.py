import unittest


from model.map.province import Province
from model.realm.realm import Realm


class RealmRemoveProvinceTest(unittest.TestCase):

    def test_remove_province(self):
        realm = Realm()
        
        province0 = Province(None, 0,0)
        realm.add_province(province0)
        
        province1 = Province(None, 1,0)
        realm.add_province(province1)
        
        self.assertTrue(realm.remove_province(province0))        
        self.assertEqual(len(realm.provinces), 1)
        self.assertEqual(province0.realm, None)
        self.assertFalse(province0 in realm.provinces)
        
        self.assertTrue(realm.remove_province(province1))        
        self.assertEqual(len(realm.provinces), 0)
        self.assertEqual(province1.realm, None)
        self.assertFalse(province1 in realm.provinces)
    
    def test_second_time(self):    
        realm = Realm()
        
        province = Province(None, 0,0)
        realm.add_province(province)
        
        realm.remove_province(province)
        self.assertFalse(realm.remove_province(province))        
        self.assertEqual(len(realm.provinces), 0)
        self.assertEqual(province.realm, None)
        self.assertFalse(province in realm.provinces)
    
    def test_invalid_province(self): 
        realm = Realm()
        
        self.assertRaises(AssertionError, realm.add_province, None)


def get_tests():
    return unittest.makeSuite(RealmRemoveProvinceTest, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())        
