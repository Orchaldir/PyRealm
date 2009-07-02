import pyglet
from pyglet.gl import *


from model.army.army import Army
from model.army.move import can_move_army, MoveArmy
from model.map.map import Map
from model.map.province import Province
from model.map.terrain import Terrain
from model.realm.realm import Realm
from view.mapview import MapView

selected_army = None

if __name__ == '__main__':
    window = pyglet.window.Window(800, 600, 'PyRealm 01')
    
    terrain0 = Terrain("Plain", 0, 255, 0)
    
    gamemap = Map()
    gamemap.create(terrain0, 8, 7)
    
    realm = Realm(255, 0, 0)
    realm.add_province(gamemap.get_province(2, 2))
    realm.add_province(gamemap.get_province(2, 3))
    
    army0 = Army(realm, 10)
    army1 = Army(realm, 10)
    army2 = Army(realm, 10)
    army3 = Army(realm, 10)
    gamemap.get_province(2, 2).add_army(army0)
    gamemap.get_province(2, 2).add_army(army1)
    gamemap.get_province(2, 2).add_army(army2)
    gamemap.get_province(2, 2).add_army(army3)
    
    view = MapView(gamemap, 50.0, 5.0, 5.0, 15.0)
    
    @window.event
    def on_draw():
        window.clear()
        glLoadIdentity()
        view.draw()
    
    @window.event
    def on_mouse_press(x, y, button, modifiers):
        global selected_army
        
        selection = view.get_province(x, y)
        
        if isinstance(selection, Army):
            selected_army = selection
        else:
            selected_army = None
        
    @window.event
    def on_mouse_release(x, y, button, modifiers):
        global selected_army
        
        selection = view.get_province(x, y)
        
        if isinstance(selection, Province) and selected_army:
            if can_move_army(selected_army, selection):
                move = MoveArmy(selected_army, selection)
                move.execute()
                view.create_batch()
            
  
    pyglet.app.run()
