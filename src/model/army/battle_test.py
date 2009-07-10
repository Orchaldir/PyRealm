import unittest


from model.army.army import Army
from model.army.battle import Battle
from model.map.province import Province
from model.realm.realm import Realm


class BattleTest(unittest.TestCase):

    def test_zero_wins(self): 
        army0 = Army()
        army0.size = 10
        army1 = Army()
        army1.size = 4
        province = Province(None, 1, 1)
        province.add_army(army0)
        province.add_army(army1)
        
        battle = Battle(army0, army1)
        
        self.assertEqual(army0.size, 6)
        self.assertEqual(army1.size, 0)
        
        self.assertEqual(army0.province, province)
        self.assertTrue(army0 in province.armies)
        self.assertEqual(army1.province, None)
        self.assertFalse(army1 in province.armies)
    
    def test_one_wins(self): 
        army0 = Army()
        army0.size = 6
        army1 = Army()
        army1.size = 10
        province = Province(None, 1, 1)
        province.add_army(army0)
        province.add_army(army1)
        
        battle = Battle(army0, army1)
        
        self.assertEqual(army0.size, 0)
        self.assertEqual(army1.size, 4)
        
        self.assertEqual(army0.province, None)
        self.assertFalse(army0 in province.armies)
        self.assertEqual(army1.province, province)
        self.assertTrue(army1 in province.armies)
    
    def test_even(self): 
        army0 = Army()
        army0.size = 5
        army1 = Army()
        army1.size = 5
        province = Province(None, 1, 1)
        province.add_army(army0)
        province.add_army(army1)
        
        battle = Battle(army0, army1)
        
        self.assertEqual(army0.size, 0)
        self.assertEqual(army1.size, 0)
        
        self.assertEqual(army0.province, None)
        self.assertFalse(army0 in province.armies)
        self.assertEqual(army1.province, None)
        self.assertFalse(army1 in province.armies)
    
    def test_invalid_army(self): 
        army = Army()
        
        self.assertRaises(AssertionError, Battle, army, None)
        self.assertRaises(AssertionError, Battle, None, army)
        self.assertRaises(AssertionError, Battle, None, None)
    
    def test_same_army(self): 
        army = Army()
        
        self.assertRaises(AssertionError, Battle, army, army)
           

def get_tests():
    return unittest.makeSuite(BattleTest, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests()) 
