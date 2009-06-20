import unittest


from model.map.province import Province


class Province_Test(unittest.TestCase):

    def test_init(self):
        province = Province(2, 4)
        self.assertEqual(province.x, 2)
        self.assertEqual(province.y, 4)


def get_tests():
    return unittest.makeSuite(Province_Test, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())  
