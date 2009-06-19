import pyglet


if __name__ == '__main__':
    window = pyglet.window.Window(800, 600, 'PyRealm 01')
    
    @window.event
    def on_draw():
        window.clear()
  
    pyglet.app.run()
