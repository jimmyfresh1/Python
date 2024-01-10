from classes.character import Character
class Pirate(Character):

    def attack ( self , ninja ):
        ninja.health -= self.strength
        return self

