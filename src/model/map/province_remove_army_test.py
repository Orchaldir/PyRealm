import unittest


from model.army.army import Army
from model.map.province import Province


class ProvinceRemoveArmyTest(unittest.TestCase):

    def test_remove_army(self):
        province = Province(None, 2, 4)
        army0 = Army(None, 10)
        army1 = Army(None, 10)
        
        province.add_army(army0)
        province.add_army(army1)
        
        self.assertTrue(province.remove_army(army0))
        self.assertTrue(province.remove_army(army1))
        
        self.assertEqual(len(province.armies), 0)
        self.assertFalse(army0 in province.armies)
        self.assertFalse(army1 in province.armies)
        self.assertEqual(army0.province, None)
        self.assertEqual(army1.province, None)
    
    def test_second_time(self):
        province = Province(None, 2, 4)
        army = Army(None, 10)
        
        province.add_army(army)
        self.assertTrue(province.remove_army(army))
        self.assertFalse(province.remove_army(army))
        self.assertEqual(len(province.armies), 0)
        self.assertFalse(army in province.armies)
        self.assertEqual(army.province, None)
    
    def test_invalid_army(self):
        province = Province(None, 2, 4)
        
        self.assertRaises(AssertionError, province.remove_army, None)


def get_tests():
    return unittest.makeSuite(ProvinceRemoveArmyTest, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())  
