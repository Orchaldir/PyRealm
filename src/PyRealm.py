import pyglet
from pyglet.gl import *
from pyglet.window import key


from model.army.army import Army
from model.army.create import can_create_army, CreateArmy
from model.army.move import can_move_army, MoveArmy
from model.map.map import Map
from model.map.province import Province
from model.map.terrain import Terrain
from model.realm.realm import Realm
from view.mapview import MapView

selected_army = None
selected_province = None

if __name__ == '__main__':
    window = pyglet.window.Window(800, 600, 'PyRealm 01')
    
    terrain0 = Terrain("Plain", 0, 255, 0)
    
    gamemap = Map()
    gamemap.create(terrain0, 8, 7)
    
    realm = Realm(255, 0, 0)
    realm.add_province(gamemap.get_province(2, 2))
    realm.add_province(gamemap.get_province(2, 3))
    
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
                move = MoveArmy(selected_army, selection)
                move.execute()
                view.create_batch()
        elif isinstance(selection, Province):
            selected_province = selection
    
    @window.event
    def on_key_release(symbol, modifiers):
        if symbol == key.C:
            if selected_province:
                if can_create_army(realm, selected_province, 1):
                    create = CreateArmy(realm, selected_province, 1)
                    create.execute()
                    view.create_batch()
  
    pyglet.app.run()
