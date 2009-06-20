import unittest


import model.map.map_test
import model.map.province_test


if __name__ == "__main__":
    suites = []

    suites.append(model.map.map_test.get_tests())
    suites.append(model.map.province_test.get_tests())

    suite = unittest.TestSuite(suites)
    
    runner = unittest.TextTestRunner()
    runner.run(suite)  
