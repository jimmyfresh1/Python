from classes.ninja import Ninja
from classes.pirate import Pirate

def Match():
    # print(input1)
    print('whats your name')
    x =input()
    newNinja= Ninja(x)
    print(newNinja)

    jack_sparrow = Pirate("Jack Sparrow")
    while jack_sparrow.health > 0:
        decision = input("What do you want to do? Attack ")
        if decision=='A':
            newNinja.attack(jack_sparrow)
            jack_sparrow.show_stats()
            continue     
    if jack_sparrow.health<=0:
        play_again=input("You won! You killed the best pirate who ever lived. Play again?\n")
        if play_again == 'Y':
            Match()
Match() 

# jack_sparrow.attack(newNinja)
# newNinja.show_stats()