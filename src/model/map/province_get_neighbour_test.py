import unittest


from model.map.map import Map
from model.map.province import Province


class ProvinceGetNeighbourTest(unittest.TestCase):

    def test_get_neighbour(self):
        test_map = Map()
        test_map.create(None, 3, 4)
        
        province = test_map.get_province(1, 1)
        
        self.assertEqual(test_map.get_province(2, 1), province.get_neighbour(0))
        self.assertEqual(test_map.get_province(2, 2), province.get_neighbour(1)) 
        self.assertEqual(test_map.get_province(1, 2), province.get_neighbour(2))
        self.assertEqual(test_map.get_province(0, 1), province.get_neighbour(3))
        self.assertEqual(test_map.get_province(1, 0), province.get_neighbour(4))
        self.assertEqual(test_map.get_province(2, 0), province.get_neighbour(5))
        
        province = test_map.get_province(1, 2)
        
        self.assertEqual(test_map.get_province(2, 2), province.get_neighbour(0))
        self.assertEqual(test_map.get_province(1, 3), province.get_neighbour(1)) 
        self.assertEqual(test_map.get_province(0, 3), province.get_neighbour(2))
        self.assertEqual(test_map.get_province(0, 2), province.get_neighbour(3))
        self.assertEqual(test_map.get_province(0, 1), province.get_neighbour(4))
        self.assertEqual(test_map.get_province(1, 1), province.get_neighbour(5))
    
    def test_invalid_province(self):
        province = Province(None, 1, 1)
        
        self.assertRaises(AssertionError, province.get_neighbour, -1)
        self.assertRaises(AssertionError, province.get_neighbour, 6)
        self.assertRaises(AssertionError, province.get_neighbour, None)


def get_tests():
    return unittest.makeSuite(ProvinceGetNeighbourTest, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())  
