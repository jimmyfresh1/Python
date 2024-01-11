from pets import Pet
from pets import Parrot
class Ninja:
    def __init__ (self, firn, treats, pf, pet):
        self.name=firn
        self.treats=treats
        self.pet =pet
        self.pf=pf

    
    def walk(self):
        self.pet.play()
    def feed(self):
        self.pet.eat()
    def bathe(self):
        self.pet.noise()

james = Ninja('james', 'bones', 'steak', 'Fido')
james.pet = Pet('Fido', 'fire', 'roll', 100, 100)
print (james.name)
print (james.pet.health)
james.walk()
james.feed()
james.bathe()
print (james.pet.health)
print (james.pet.energy)
james.pet=Parrot('Tattletale', 'Total Snitch', 'Ruin My Marriage', 'None after Im Done with Him', 'fertilizer, soon enough')
print(james.pet.name,)
print(james.pet.tricks)