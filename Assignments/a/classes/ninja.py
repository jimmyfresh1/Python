from classes.character import Character
class Ninja(Character):


    def attack( self , pirate ):
        pirate.health -= self.strength
        return self