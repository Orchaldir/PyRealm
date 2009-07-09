import unittest


from utility.color import Color


class ColorTest(unittest.TestCase):

    def test_get(self):
        color = Color(0.1, 0.2, 0.3)
        
        self.assertEqual(color.get_r(), 0.1)
        self.assertEqual(color.get_g(), 0.2)
        self.assertEqual(color.get_b(), 0.3)
        self.assertEqual(color.get_a(), 1.0)
        
        color = Color(0.4, 0.3, 0.2, 0.1)
        
        self.assertEqual(color.get_r(), 0.4)
        self.assertEqual(color.get_g(), 0.3)
        self.assertEqual(color.get_b(), 0.2)
        self.assertEqual(color.get_a(), 0.1)
    
    def test_get_int(self):
        color = Color(0.4, 0.3, 0.2, 0.1)
        
        self.assertEqual(color.get_int_r(), 102)
        self.assertEqual(color.get_int_g(), 76)
        self.assertEqual(color.get_int_b(), 51)
        self.assertEqual(color.get_int_a(), 25)
    
    def test_out_of_range(self):
        self.assertRaises(AssertionError, Color, -1.0, 0.0, 0.0)
        self.assertRaises(AssertionError, Color, 20.0, 0.0, 0.0)
        
        self.assertRaises(AssertionError, Color, 0.0, -1.0, 0.0)
        self.assertRaises(AssertionError, Color, 0.0, 20.0, 0.0)
        
        self.assertRaises(AssertionError, Color, 0.0, 0.0, -1.0)
        self.assertRaises(AssertionError, Color, 0.0, 0.0, 20.0)
        
        self.assertRaises(AssertionError, Color, 0.0, 0.0, 0.0, -1.0)
        self.assertRaises(AssertionError, Color, 0.0, 0.0, 0.0, 20.0)
    
    def test_invalid_value(self):
        self.assertRaises(AssertionError, Color, None, 0.0, 0.0, 0.0)
        self.assertRaises(AssertionError, Color, 0.0, None, 0.0, 0.0)
        self.assertRaises(AssertionError, Color, 0.0, 0.0, None, 0.0)
        self.assertRaises(AssertionError, Color, 0.0, 0.0, 0.0, None)


def get_tests():
    return unittest.makeSuite(ColorTest, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())    
