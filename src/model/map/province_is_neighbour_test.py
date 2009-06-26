import unittest


from model.map.province import Province


class ProvinceIsNeighbourTest(unittest.TestCase):

    def test_is_neighbour(self):
        province = Province(None, 1, 1)
        
        self.assertTrue(province.is_neighbour(Province(None, 2, 1)))
        self.assertTrue(province.is_neighbour(Province(None, 2, 2)))
        self.assertTrue(province.is_neighbour(Province(None, 1, 2)))
        self.assertTrue(province.is_neighbour(Province(None, 0, 1)))
        self.assertTrue(province.is_neighbour(Province(None, 1, 0)))
        self.assertTrue(province.is_neighbour(Province(None, 2, 0)))
        
        province = Province(None, 1, 2)
        
        self.assertTrue(province.is_neighbour(Province(None, 2, 2)))
        self.assertTrue(province.is_neighbour(Province(None, 1, 3)))
        self.assertTrue(province.is_neighbour(Province(None, 0, 3)))
        self.assertTrue(province.is_neighbour(Province(None, 0, 2)))
        self.assertTrue(province.is_neighbour(Province(None, 0, 1)))
        self.assertTrue(province.is_neighbour(Province(None, 1, 1)))
    
    def test_is_not_neighbour(self):
        province = Province(None, 1, 1)
        
        self.assertFalse(province.is_neighbour(Province(None, 0, 0)))
        
        province = Province(None, 1, 2)
        
        self.assertFalse(province.is_neighbour(Province(None, 0, 0)))
    
    def test_invalid_province(self):
        province = Province(None, 1, 1)
        
        self.assertRaises(AssertionError, province.is_neighbour, None)


def get_tests():
    return unittest.makeSuite(ProvinceIsNeighbourTest, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())  
