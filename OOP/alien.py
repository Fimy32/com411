from inhabitant import Inhabitant
from JetPack import JetPack
from Laser import Laser

class Alien(Inhabitant):
    def __init__(self, name):
        Inhabitant.__init__(self, name)
        self.technology = [JetPack(), Laser(100)]
