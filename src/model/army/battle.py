

class Battle:

    def __init__(self, army0, army1):
        assert army0, 'Invalid army!'
        assert army1, 'Invalid army!'
        assert army0 != army1, 'Same army!'
        assert army0.realm != army1.realm, 'Same realm!'
        
        self.army0 = army0
        self.army1 = army1
        
        self.province = army0.province
        
        min_size = min(self.army0.size, self.army1.size)
        
        self.army0.size -= min_size
        self.army1.size -= min_size
        
        if self.army0.size is 0:
            self.army0.remove()
        
        if self.army1.size is 0:
            self.army1.remove()
