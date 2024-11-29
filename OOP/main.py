from universe import *
from alien import *
if __name__ == "__main__":
    universe1 = Universe()
    universe1.show_population_grapth("")

    alien1 = Alien("Bob")
    print(alien1.technology)
    print(alien1.technology[0].fly(100))