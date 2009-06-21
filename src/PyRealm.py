import pyglet
from pyglet.gl import *


from model.map.map import Map
from model.map.terrain import Terrain
from model.realm.realm import Realm
from view.mapview import MapView


if __name__ == '__main__':
    window = pyglet.window.Window(800, 600, 'PyRealm 01')
    
    terrain0 = Terrain("Plain", 0, 255, 0)
    
    gamemap = Map()
    gamemap.create(terrain0, 8, 7)
    
    realm = Realm(255, 0, 0)
    realm.add_province(gamemap.get_province(2, 2))
    realm.add_province(gamemap.get_province(2, 3))
    
    view = MapView(gamemap, 50.0, 5.0)
    
    @window.event
    def on_draw():
        window.clear()
        glLoadIdentity()
        glTranslated(400, 200, 0)
        view.draw()
  
    pyglet.app.run()
