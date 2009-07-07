import unittest


from model.army.army import Army
from model.army.increase import can_increase_army, IncreaseArmy
from model.realm.realm import Realm


class CanIncreaseArmyTest(unittest.TestCase):

    def test_can_increase_army(self): 
        realm = Realm()    
        army = Army(realm, 10)
        
        self.assertTrue(can_increase_army(realm, army))
    
    def test_invalid_army(self):
        realm = Realm()    
        
        self.assertRaises(AssertionError, can_increase_army, realm, None)
    
    def test_invalid_realm(self):
        realm = Realm()    
        army = Army(realm, 10)
        
        self.assertRaises(AssertionError, can_increase_army, None, army)
    
    def test_wrong_realm(self):
        realm0 = Realm()    
        realm1 = Realm()
        army = Army(realm0, 10)
        
        self.assertFalse(can_increase_army(realm1, army))   
        


class IncreaseArmyTest(unittest.TestCase):

    def test_move(self):     
        realm = Realm()    
        army = Army(realm, 10)
        
        increase = IncreaseArmy(realm, army)
        increase.execute()
        
        self.assertEqual(army.size, 11)
        

def get_tests():
    return [unittest.makeSuite(CanIncreaseArmyTest, 'test'), unittest.makeSuite(IncreaseArmyTest, 'test')]


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())          
        
