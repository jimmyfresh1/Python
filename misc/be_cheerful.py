def be_cheerful(name):
    print(f"Good Morning {name}")
be_cheerful("Adrien")

#Note here you've given it a parameter. Therefore if you try to call the function without an argument, it won't work. BUT, rather than using a parameter...

def be_cheerful2(name='dog'):
    print (f'Good Morning {name}')
be_cheerful2()
be_cheerful2('swine')

#You can have the default argument, or put in an argument of your own. Now if you want to do other cool things...

def be_cheerful2(name='dog',repeat=2):
    print (f'Good Morning {name}' * repeat)
be_cheerful2()
be_cheerful2('swine')

#add in \n for line break if you want 

be_cheerful2('swine', 4)

#you can have arguments out of order so long as you specify arguments to replace the defaults. this is called naming arguments.

be_cheerful2(repeat=5, name='cuckoo')

#note that unnamed arguments will be evaluated in order