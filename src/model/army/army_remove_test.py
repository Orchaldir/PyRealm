import unittest


from model.army.army import Army
from model.map.province import Province


class ArmyRemoveTest(unittest.TestCase):

    def test_remove(self): 
        army = Army(None)
        province = Province(None, 1, 1)
        province.add_army(army)
        
        army.remove()
        
        self.assertEqual(army.province, None)
        self.assertFalse(army in province.armies)
           

def get_tests():
    return unittest.makeSuite(ArmyRemoveTest, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests()) 
