from classes.ninja import Ninja
from classes.pirate import Pirate

# //input1=p, n input2=name
# nameClassconstruct, where Class= based on n or p

# p1class = input('')
# p1name = input('')

# p2class = input('')
# p2name =input('')

# print(p1class)
# print(p1name)

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

michelangelo.attack(jack_sparrow)
jack_sparrow.show_stats()

