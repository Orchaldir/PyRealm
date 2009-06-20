import pyglet
from pyglet.gl import *


from model.map.map import Map
from view.mapview import MapView


if __name__ == '__main__':
    window = pyglet.window.Window(800, 600, 'PyRealm 01')
    
    gamemap = Map()
    gamemap.create(8, 7)
    view = MapView(gamemap, 50.0, 2.0)
    
    @window.event
    def on_draw():
        window.clear()
        glLoadIdentity()
        glTranslated(400, 200, 0)
        view.draw()
  
    pyglet.app.run()
