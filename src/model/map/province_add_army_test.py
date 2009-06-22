import unittest


from model.combat.army import Army
from model.map.province import Province


class Province_add_army_Test(unittest.TestCase):

    def test_add_army(self):
        province = Province(None, 2, 4)
        army0 = Army(None, 10)
        army1 = Army(None, 10)
        
        self.assertTrue(province.add_army(army0))
        self.assertTrue(province.add_army(army1))
        self.assertEqual(len(province.armies), 2)
        self.assertTrue(army0 in province.armies)
        self.assertTrue(army1 in province.armies)
    
    def test_second_time(self):
        province = Province(None, 2, 4)
        army = Army(None, 10)
        
        self.assertTrue(province.add_army(army))
        self.assertFalse(province.add_army(army))
        self.assertEqual(len(province.armies), 1)
        self.assertTrue(army in province.armies)
    
    def test_invalid_army(self):
        province = Province(None, 2, 4)
        
        self.assertFalse(province.add_army(None))


def get_tests():
    return unittest.makeSuite(Province_add_army_Test, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())  
