import unittest


import model.army.create_test
import model.army.move_test
import model.map.create_test
import model.map.map_test
import model.map.map_get_province_test
import model.map.province_add_army_test
import model.map.province_get_neighbour_test
import model.map.province_is_neighbour_test
import model.map.province_remove_army_test
import model.realm.realm_add_province_test
import model.realm.realm_create_army_test
import model.realm.realm_remove_province_test
import model.time.time_test


if __name__ == "__main__":
    suites = []

    suites.extend(model.army.create_test.get_tests())
    suites.extend(model.army.move_test.get_tests())
    suites.extend(model.map.create_test.get_tests())
    suites.extend(model.map.map_test.get_tests())
    suites.extend(model.map.map_get_province_test.get_tests())
    suites.extend(model.map.province_add_army_test.get_tests())
    suites.extend(model.map.province_get_neighbour_test.get_tests())
    suites.extend(model.map.province_is_neighbour_test.get_tests())
    suites.extend(model.map.province_remove_army_test.get_tests())
    suites.extend(model.realm.realm_add_province_test.get_tests())    
    suites.extend(model.realm.realm_create_army_test.get_tests())    
    suites.extend(model.realm.realm_remove_province_test.get_tests())
    suites.extend(model.time.time_test.get_tests())

    suite = unittest.TestSuite(suites)
    
    runner = unittest.TextTestRunner()
    runner.run(suite)  
