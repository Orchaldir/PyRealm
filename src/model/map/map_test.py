import unittest


from model.map.map import Map


class Map_Test(unittest.TestCase):

    def test_create(self):
        test_map = Map()
        test_map.create(2, 4)
        self.assertEqual(test_map.width, 2)
        self.assertEqual(test_map.height, 4)
        self.assertEqual(len(test_map.provinces), 8)
        
        for x in range(0, 2):
            for y in range(0, 4):
                province = test_map.get_province(x,y)
                self.assertEqual(province.x, x)
                self.assertEqual(province.y, y)
    
    def test_get_province(self):
        test_map = Map()
        test_map.create(2, 4)
        
        for x in range(0, 2):
            for y in range(0, 4):
                self.assertEqual(test_map.get_province(x,y), test_map.provinces[(x, y)])
    
    def test_get_province_outside(self):
        test_map = Map()
        test_map.create(2, 4)
        
        self.assertEqual(test_map.get_province(-1,0), None)
        self.assertEqual(test_map.get_province(2,0), None)
        self.assertEqual(test_map.get_province(0,-1), None)
        self.assertEqual(test_map.get_province(0,4), None)


def get_tests():
    return unittest.makeSuite(Map_Test, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())          
        
