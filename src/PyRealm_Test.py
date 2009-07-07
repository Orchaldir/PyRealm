import unittest


import model.army.army_remove_test
import model.army.battle_test
import model.army.create_test
import model.army.increase_test
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
import model.world_create_realm_test
import model.world_get_realm_test
import model.world_tick_test


if __name__ == "__main__":
    suites = []

    suites.extend(model.army.army_remove_test.get_tests())
    suites.extend(model.army.battle_test.get_tests())
    suites.extend(model.army.create_test.get_tests())
    suites.extend(model.army.increase_test.get_tests())
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
    suites.extend(model.world_create_realm_test.get_tests())
    suites.extend(model.world_get_realm_test.get_tests())
    suites.extend(model.world_tick_test.get_tests())

    suite = unittest.TestSuite(suites)
    
    runner = unittest.TextTestRunner()
    runner.run(suite)  
