import unittest


from model.army.army import Army
from model.map.create import can_create_province, CreateProvince
from model.map.province import Province
from model.realm.realm import Realm


class CanCreateProvinceTest(unittest.TestCase):

    def test_can_create_province(self):     
        realm = Realm()        
        army = Army(realm, 1)
        province = Province(None, 0,0)
        province.add_army(army)
        
        self.assertTrue(can_create_province(army)) 
    
    def test_invalid_army(self):     
        self.assertRaises(AssertionError, can_create_province, None)
    
    def test_invalid_province(self):     
        realm = Realm()        
        army = Army(realm, 1)
        
        self.assertRaises(AssertionError, can_create_province, army)
   
    def test_other_realm(self):     
        realm0 = Realm()
        realm1 = Realm()
        army = Army(realm0, 1)
        province = Province(None, 0,0)
        province.add_army(army)
        realm1.add_province(province)
        
        self.assertFalse(can_create_province(army)) 
    
    def test_same_realm(self):     
        realm = Realm()
        army = Army(realm, 1)
        province = Province(None, 0,0)
        province.add_army(army)
        realm.add_province(province)
        
        self.assertFalse(can_create_province(army)) 


class CreateProvinceTest(unittest.TestCase):

    def test_create_province(self):
        realm = Realm()        
        army = Army(realm, 1)
        province = Province(None, 0,0)
        province.add_army(army)
        
        create = CreateProvince(army)
        create.execute()
        
        self.assertEqual(province.realm, realm)
        self.assertTrue(province in realm.provinces)
                
        
def get_tests():
    return [unittest.makeSuite(CanCreateProvinceTest, 'test'), unittest.makeSuite(CreateProvinceTest, 'test')]


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())     
