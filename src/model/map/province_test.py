import unittest


from model.map.map import Map
from model.map.province import Province


class Province_Test(unittest.TestCase):

    def test_init(self):
        province = Province(1, 2, 4)
        self.assertEqual(province.map, 1)
        self.assertEqual(province.x, 2)
        self.assertEqual(province.y, 4)
    
    def test_get_neighbour(self):
        test_map = Map()
        test_map.create(3, 4)
        
        province = test_map.get_province(1, 1)
        
        self.assertEqual(test_map.get_province(2, 1), province.get_neighbour(0))
        self.assertEqual(test_map.get_province(2, 2), province.get_neighbour(1)) 
        self.assertEqual(test_map.get_province(1, 2), province.get_neighbour(2))
        self.assertEqual(test_map.get_province(0, 1), province.get_neighbour(3))
        self.assertEqual(test_map.get_province(1, 0), province.get_neighbour(4))
        self.assertEqual(test_map.get_province(2, 0), province.get_neighbour(5))
        self.assertEqual(None, province.get_neighbour(6))
        
        province = test_map.get_province(1, 2)
        
        self.assertEqual(test_map.get_province(2, 2), province.get_neighbour(0))
        self.assertEqual(test_map.get_province(1, 3), province.get_neighbour(1)) 
        self.assertEqual(test_map.get_province(0, 3), province.get_neighbour(2))
        self.assertEqual(test_map.get_province(0, 2), province.get_neighbour(3))
        self.assertEqual(test_map.get_province(0, 1), province.get_neighbour(4))
        self.assertEqual(test_map.get_province(1, 1), province.get_neighbour(5))
        self.assertEqual(None, province.get_neighbour(6))
    
    def test_is_neighbour(self):
        test_map = Map()
        test_map.create(3, 4)
        
        province = test_map.get_province(1, 1)
        
        self.assertTrue(province.is_neighbour(test_map.get_province(2, 1)))
        self.assertTrue(province.is_neighbour(test_map.get_province(2, 2)))
        self.assertTrue(province.is_neighbour(test_map.get_province(1, 2)))
        self.assertTrue(province.is_neighbour(test_map.get_province(0, 1)))
        self.assertTrue(province.is_neighbour(test_map.get_province(1, 0)))
        self.assertTrue(province.is_neighbour(test_map.get_province(2, 0)))
        
        self.assertFalse(province.is_neighbour(test_map.get_province(0, 0)))
        
        province = test_map.get_province(1, 2)
        
        self.assertTrue(province.is_neighbour(test_map.get_province(2, 2)))
        self.assertTrue(province.is_neighbour(test_map.get_province(1, 3)))
        self.assertTrue(province.is_neighbour(test_map.get_province(0, 3)))
        self.assertTrue(province.is_neighbour(test_map.get_province(0, 2)))
        self.assertTrue(province.is_neighbour(test_map.get_province(0, 1)))
        self.assertTrue(province.is_neighbour(test_map.get_province(1, 1)))
        
        self.assertFalse(province.is_neighbour(test_map.get_province(0, 0)))


def get_tests():
    return unittest.makeSuite(Province_Test, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())  
