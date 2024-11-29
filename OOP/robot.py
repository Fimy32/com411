from inhabitant import Inhabitant

class Robot(Inhabitant):

    def __init__(self, name):

        Inhabitant.__init__(self, name)

        self.laws = "Do Not Kill"

    def the_laws(self,):
        pass

