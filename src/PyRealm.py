import pyglet
from pyglet.gl import *
from pyglet.window import key


from model.army.army import Army
from model.army.create import can_create_army, CreateArmy
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
realm = None
realm_index = 0

if __name__ == '__main__':
    window = pyglet.window.Window(800, 600, 'PyRealm 01')
    
    terrain0 = Terrain("Plain", 0.0, 1.0, 0.0)
    
    world = World()
    
    gamemap = Map()
    gamemap.create(terrain0, 3, 3)
    
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
        global selected_army, selected_province
        
        selection = view.get_province(x, y)
        
        selected_army = None
        selected_province = None
        
        if isinstance(selection, Army):
            selected_army = selection
        
    @window.event
    def on_mouse_release(x, y, button, modifiers):
        global selected_army, selected_province
        
        selection = view.get_province(x, y)
        
        if isinstance(selection, Province) and selected_army:
            if can_move_army(selected_army, selection):
                selected_army.action = MoveArmy(selected_army, selection)
        elif isinstance(selection, Province):
            selected_province = selection
    
    @window.event
    def on_key_release(symbol, modifiers):
        global realm, realm_index
        if symbol == key.C:
            if selected_province:
                if can_create_army(realm, selected_province, 1):
                    selected_province.action = CreateArmy(realm, selected_province, 1)
            elif selected_army:
                if can_create_province(selected_army):
                    selected_army.action = CreateProvince(selected_army)                    
        elif symbol == key.SPACE:
            realm_index += 1
            realm = world.get_realm(realm_index)
            
            if not realm:
                realm_index = 0
                realm = world.get_realm(realm_index)
                world.tick()
                view.create_batch()
                print('Turn={0:03d}'.format(world.turn))
                print('Realm={0:s}:'.format(realm.name))
            else:
                print('Realm={0:s}:'.format(realm.name))
  
    pyglet.app.run()
