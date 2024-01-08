num1 = 42 #Primitive Data Type Number 
num2 = 2.3 #Primitive Data Type Number 
boolean = True #Primitive Data Type Boolean
string = 'Hello World' #Primitive Data Type String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #Composite Type List, initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Composite Type Dictionary, , initialize
fruit = ('blueberry', 'strawberry', 'banana') #Composite Type Tuple, , initialize
print(type(fruit)) #type check
print(pizza_toppings[1]) #access value 1 of list, log statement
pizza_toppings.append('Mushrooms') #add value 'Mushrooms' to end
print(person['name']) #access value name in dictionary
person['name'] = 'George'  #change value name in dictionary
person['eye_color'] = 'blue' #add value eye_color to dicitonary
print(fruit[2]) #access tuple value at index 2

if num1 > 45: #if conditional
    print("It's greater") #log statement 
else: #else conditional
    print("It's lower") #log statement 

if len(string) < 5: #length check, 
    print("It's a short word!") #log statement 
elif len(string) > 15: #else if 
    print("It's a long word!") #log statement 
else: #else
    print("Just right!") #log statement 

for x in range(5): #for loop from 0 to 4
    print(x) #log statement 
for x in range(2,5): #for loop from 2 to 4
    print(x) #log statement 
for x in range(2,10,3): #for loop from 2 to 10, increments of 3
    print(x) #log statement 
x = 0 # variable declaration and also the starting value of while loop
while(x < 5): #while loop, starts at 0, stops  when x becomes equal to or greater htan five 
    print(x) #log statement 
    x += 1 #while loop increment

pizza_toppings.pop() #list delete value
pizza_toppings.pop(1)

print(person) #log statement 
person.pop('eye_color') #dictionary delete v alue 
print(person) #log statement 

for topping in pizza_toppings: # for loop, iterating over a sequence
    if topping == 'Pepperoni':   #if statement
        continue #continue statement, which terminates this iteration of the loop
    print('After 1st if statement') #log statement
    if topping == 'Olives': #if statement 
        break #function break, which terminates the entire loop

def print_hello_ten_times(): #function declaration
    for num in range(10): #for loop from 0 to 9
        print('Hello') #log statement 

print_hello_ten_times() # function call

def print_hello_x_times(x): # x is  a parameter
    for num in range(x): # for statement
        print('Hello') #log statement 

print_hello_x_times(4) #function call with argument 4 

def print_hello_x_or_ten_times(x = 10): #x=10 is an argument
    for num in range(x): #for statement
        print('Hello') #log statement 

print_hello_x_or_ten_times() #function call
print_hello_x_or_ten_times(4) #function call with argument 4


"""
Bonus section
"""

# print(num3)  #NameError, name num3 is not assigned (assuming this is in order)
# num3 = 72 
# fruit[0] = 'cranberry'
# print(person['favorite_team']) #KeyError 
# print(pizza_toppings[7]) #list index out of range
#   print(boolean) #unexpected indent
# fruit.append('raspberry') #Type Error, tuple etc., #attributeerror, no attribute append 
# fruit.pop(1) #tuple object has no value 'pop'