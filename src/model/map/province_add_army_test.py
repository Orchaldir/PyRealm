import unittest


from model.combat.army import Army
from model.map.province import Province


class ProvinceAddArmyTest(unittest.TestCase):

    def test_add_army(self):
        province = Province(None, 2, 4)
        army0 = Army(None, 10)
        army1 = Army(None, 10)
        
        self.assertTrue(province.add_army(army0))
        self.assertTrue(province.add_army(army1))
        self.assertEqual(len(province.armies), 2)
        self.assertTrue(army0 in province.armies)
        self.assertTrue(army1 in province.armies)
        self.assertEqual(army0.province, province)
        self.assertEqual(army1.province, province)
    
    def test_second_time(self):
        province = Province(None, 2, 4)
        army = Army(None, 10)
        
        self.assertTrue(province.add_army(army))
        self.assertFalse(province.add_army(army))
        self.assertEqual(len(province.armies), 1)
        self.assertTrue(army in province.armies)
        self.assertEqual(army.province, province)
    
    def test_other_province(self):
        province0 = Province(None, 2, 4)
        province1 = Province(None, 2, 5)
        army = Army(None, 10)
        
        self.assertTrue(province0.add_army(army))
        self.assertFalse(province1.add_army(army))
        self.assertEqual(len(province0.armies), 1)
        self.assertEqual(len(province1.armies), 0)
        self.assertTrue(army in province0.armies)
        self.assertFalse(army in province1.armies)
        self.assertEqual(army.province, province0)
    
    def test_invalid_army(self):
        province = Province(None, 2, 4)
        
        self.assertRaises(AssertionError, province.add_army, None)


def get_tests():
    return unittest.makeSuite(ProvinceAddArmyTest, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())  
