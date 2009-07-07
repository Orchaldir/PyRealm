import unittest


from model.army.army import Army
from model.army.move import can_move_army, MoveArmy
from model.map.province import Province
from model.realm.realm import Realm


class CanMoveArmyTest(unittest.TestCase):

    def test_can_move_army(self): 
        realm = Realm()    
        army = Army(realm, 10)
        province0 = Province(None, 1, 1)
        province0.add_army(army)
        
        self.assertTrue(can_move_army(realm, army, Province(None, 2, 1)))
        self.assertTrue(can_move_army(realm, army, Province(None, 2, 2)))
        self.assertTrue(can_move_army(realm, army, Province(None, 1, 2)))
        self.assertTrue(can_move_army(realm, army, Province(None, 0, 1)))
        self.assertTrue(can_move_army(realm, army, Province(None, 1, 0)))
        self.assertTrue(can_move_army(realm, army, Province(None, 2, 0)))
        
        province0.remove_army(army)
        province1 = Province(None, 1, 2)
        province1.add_army(army)
        
        self.assertTrue(can_move_army(realm, army, Province(None, 2, 2)))
        self.assertTrue(can_move_army(realm, army, Province(None, 1, 3)))
        self.assertTrue(can_move_army(realm, army, Province(None, 0, 3)))
        self.assertTrue(can_move_army(realm, army, Province(None, 0, 2)))
        self.assertTrue(can_move_army(realm, army, Province(None, 0, 1)))
        self.assertTrue(can_move_army(realm, army, Province(None, 1, 1)))
    
    def test_invalid_province(self):
        realm = Realm()    
        army = Army(realm, 10)
        province = Province(None, 1, 1)
        province.add_army(army)
        
        self.assertRaises(AssertionError, can_move_army, realm, army, None)
    
    def test_invalid_army(self):
        realm = Realm()    
        army = Army(realm, 10)
        province = Province(None, 1, 1)
        
        self.assertRaises(AssertionError, can_move_army, realm, None, province)              
        self.assertFalse(can_move_army(realm, army, province))
    
    def test_invalid_realm(self):
        realm = Realm()    
        army = Army(realm, 10)
        province = Province(None, 1, 1)
        province.add_army(army)
        
        self.assertRaises(AssertionError, can_move_army, None, army, Province(None, 2, 1))
    
    def test_wrong_realm(self):
        realm0 = Realm()    
        realm1 = Realm()
        army = Army(realm0, 10)
        province = Province(None, 1, 1)
        province.add_army(army)
        
        self.assertFalse(can_move_army(realm1, army, Province(None, 2, 1)))
    
    def test_not_neighbour(self):     
        realm = Realm()    
        army = Army(realm, 10)
        province = Province(None, 1, 1)
        province.add_army(army)
        
        self.assertFalse(can_move_army(realm, army, Province(None, 0, 0)))
        self.assertFalse(can_move_army(realm, army, Province(None, 0, 2)))
        self.assertFalse(can_move_army(realm, army, Province(None, 3, 2)))
        self.assertFalse(can_move_army(realm, army, Province(None, 3, 0)))       


class MoveArmyTest(unittest.TestCase):

    def test_move(self):     
        realm = Realm()    
        army = Army(realm, 10)
        province0 = Province(None, 1, 1)
        province1 = Province(None, 1, 2)
        
        province0.add_army(army)
        
        move = MoveArmy(realm, army, province1)
        move.execute()
        
        self.assertEqual(len(province0.armies), 0)
        self.assertEqual(len(province1.armies), 1)               
        self.assertFalse(army in province0.armies)
        self.assertTrue(army in province1.armies)
        self.assertEqual(army.province, province1)        


def get_tests():
    return [unittest.makeSuite(CanMoveArmyTest, 'test'), unittest.makeSuite(MoveArmyTest, 'test')]


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())          
        
