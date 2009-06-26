import unittest


from model.map.map import Map


class MapGetProvinceTest(unittest.TestCase):

    def test_get_province(self):
        test_map = Map()
        test_map.create(None, 2, 4)
        
        for x in range(0, 2):
            for y in range(0, 4):
                self.assertEqual(test_map.get_province(x,y), test_map.provinces[(x, y)])
    
    def test_outside(self):
        test_map = Map()
        test_map.create(None, 2, 4)
        
        self.assertEqual(test_map.get_province(-1,0), None)
        self.assertEqual(test_map.get_province(2,0), None)
        self.assertEqual(test_map.get_province(0,-1), None)
        self.assertEqual(test_map.get_province(0,4), None)


def get_tests():
    return unittest.makeSuite(MapGetProvinceTest, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())          
        
