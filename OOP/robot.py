from inhabitant import Inhabitant

class Robot(Inhabitant):

    def __init__(self, name,laws):

        Inhabitant.__init__(self, name)

        self.laws = laws

    def the_laws(self,):
        pass

