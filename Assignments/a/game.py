from classes.ninja import Ninja
from classes.pirate import Pirate


# print(input1)
print('whats your name')
x =input()
newNinja= Ninja(x)
print(newNinja)

jack_sparrow = Pirate("Jack Sparrow")


while jack_sparrow.health > 0:
    decision = input("What do you want to do? Attack")
    if decision=='A':
        newNinja.attack(jack_sparrow)
        jack_sparrow.show_stats()
        continue     


# jack_sparrow.attack(newNinja)
# newNinja.show_stats()