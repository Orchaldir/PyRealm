import unittest


from model.army.create import can_create_army, CreateArmy
from model.map.province import Province
from model.realm.realm import Realm
from model.world import World


class CanCreateArmyTest(unittest.TestCase):

    def test_can_create_army(self):     
        realm = Realm()        
        province = Province(None, 0,0)
        realm.add_province(province)
        
        self.assertTrue(can_create_army(realm, province, 1)) 
    
    def test_invalid_province(self):    
        realm = Realm()        
        province = Province(None, 0,0)
        
        self.assertFalse(can_create_army(realm, province, 1))        
        self.assertRaises(AssertionError, can_create_army, realm, None, 1)
    
    def test_invalid_realm(self):    
        province = Province(None, 0,0)
        
        self.assertRaises(AssertionError, can_create_army, None, province, 1)
    
    def test_invalid_size(self):    
        realm = Realm()        
        province = Province(None, 0,0)
        realm.add_province(province)
        
        self.assertRaises(AssertionError, can_create_army, realm, province, 0)
        self.assertRaises(AssertionError, can_create_army, realm, province, -1)
        self.assertRaises(AssertionError, can_create_army, realm, province, None)
        

class CreateArmyTest(unittest.TestCase):

    def test_create_army(self):
        world = World()
        realm = world.create_realm('Test', 1.0, 1.0, 1.0)
        province = Province(None, 0,0)
        realm.add_province(province)
        
        create0 = CreateArmy(world, realm, province, 1)
        create0.execute()
        
        army0 = create0.army
        self.assertNotEqual(army0, None)
        self.assertEqual(army0.realm, realm)
        self.assertEqual(army0.size, 1)
        self.assertEqual(army0.province, province)
        self.assertEqual(len(province.armies), 1)
        self.assertTrue(army0 in province.armies)
        self.assertEqual(len(realm.armies), 1)
        self.assertTrue(army0 in realm.armies)
        
        create1 = CreateArmy(world, realm, province, 10)
        create1.execute()
        
        army1 = create1.army
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
        
        
def get_tests():
    return [unittest.makeSuite(CanCreateArmyTest, 'test'), unittest.makeSuite(CreateArmyTest, 'test')]


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())     
