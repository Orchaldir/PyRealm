import pyglet
from pyglet.gl import *
from pyglet.window import key


from model.army.army import Army
from model.army.create import can_create_army, CreateArmy
from model.army.increase import can_increase_army, IncreaseArmy
from model.army.move import can_move_army, MoveArmy
from model.map.create import can_create_province, CreateProvince
from model.map.map import Map
from model.map.province import Province
from model.map.terrain import Terrain
from model.realm.realm import Realm
from model.world import World
from view.mapview import MapView

selected_army = None
selected_province = None
moved_army = None
realm = None
realm_index = 0

if __name__ == '__main__':
    window = pyglet.window.Window(800, 600, 'PyRealm 01')
    
    terrain0 = Terrain("Plain", 0.0, 1.0, 0.0)
    
    gamemap = Map()
    gamemap.create(terrain0, 3, 3)
    
    world = World(gamemap)
    
    realm0 = world.create_realm('Askir', 1.0, 0.0, 0.0)
    realm0.add_province(gamemap.get_province(2, 2))
    
    realm1 = world.create_realm('Thalak', 0.0, 0.0, 1.0)
    realm1.add_province(gamemap.get_province(0, 0))
    
    realm = realm0
    print('Realm={0:s}:'.format(realm.name))
    
    view = MapView(gamemap, 50.0, 5.0, 5.0, 15.0)
    
    @window.event
    def on_draw():
        window.clear()
        glLoadIdentity()
        view.draw()
    
    @window.event
    def on_mouse_press(x, y, button, modifiers):
        global moved_army
        
        selection = view.get_province(x, y)       
        
        moved_army = None        
        
        if isinstance(selection, Army):
            moved_army = selection
        
    @window.event
    def on_mouse_release(x, y, button, modifiers):
        global realm, selected_army, selected_province, moved_army
        
        selected_army = None
        selected_province = None
        
        selection = view.get_province(x, y)
        
        if isinstance(selection, Province) and moved_army:
            if can_move_army(realm, moved_army, selection):
                moved_army.action = MoveArmy(realm, moved_army, selection)
        elif isinstance(selection, Province):
            selected_province = selection
            print('Province({0:d},{1:d}): Realm={2:s}'.format(selected_province.x, selected_province.y, 
                selected_province.realm.name if selected_province.realm else 'None'))
        elif isinstance(selection, Army):
            selected_army = selection
            print('Army: Realm={0:s} Size={1:d}'.format(selected_army.realm.name, selected_army.size))
    
    @window.event
    def on_key_release(symbol, modifiers):
        global realm, realm_index
        if symbol == key.C:
            if selected_province:
                if can_create_army(realm, selected_province, 1):
                    selected_province.action = CreateArmy(realm, selected_province, 1)
            elif selected_army:
                if can_create_province(realm, selected_army):
                    selected_army.action = CreateProvince(realm, selected_army)   
        elif symbol == key.I:
            if selected_army:
                if can_increase_army(realm, selected_army):
                    selected_army.action = IncreaseArmy(realm, selected_army)                    
        elif symbol == key.SPACE:
            realm_index += 1
            realm = world.get_realm(realm_index)
            
            if not realm:
                realm_index = 0
                realm = world.get_realm(realm_index)
                result = world.tick()
                view.create_batch()
                print('Turn={0:03d}'.format(world.turn))
                
                for battle in result.battles:
                    print('Battle: Province={0:d},{1:d} {2:s} vs {3:s}'.format(battle.province.x, battle.province.y, 
                        battle.army0.realm.name, battle.army1.realm.name))
                
                print('Realm={0:s}:'.format(realm.name))
            else:
                print('Realm={0:s}:'.format(realm.name))
  
    pyglet.app.run()
