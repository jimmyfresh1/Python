#1
def number_of_food_groups():
    return 5
print('1.', number_of_food_groups())
#should be 5?

# #2
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# #won't print because you haven't defined num_yadda_week yet so you actually just have to comment this out


#3
def number_of_books_on_hold():
    return 5
    return 10
print('3.', number_of_books_on_hold())
#5, because it already returns 


#4
def number_of_fingers():
    return 5
    print(10)
print('4.', number_of_fingers())
#this will print 5 because the return value is 5, which replaces the functgion call


#5
def number_of_great_lakes():
    print('5a.', 5)
x = number_of_great_lakes()
print('5b.', x)
# 5, none. you're assigning the value of the function call to x, which also calls the function, and within the function 5 is printed. but when you print x, x has no value, because the function had no return value. so a return value of None is being stored in x 

# #6
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))
# # 3, 5, then some kind of error because you're trying to add None to None. 3 and 5 does print successfully, but code is commented out so problems after this can run 

#7
def concatenate(b,c):
    return str(b)+str(c)
print ('7. ')
print(concatenate(2,5))
#should be 25 i think... just adding the two strings together without any spacews.

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print('8a.' ,b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print('8b. ', number_of_oceans_or_fingers_or_continents())
#100, 10. first it prints b within the function. b is 100. then, since b is greater than 10, therefore the if conditional evalutes to false, the else statement runs and the function call returns 10. print then prints 10. 

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# 7, 14, 21. first one does the if, second one does the else, and then in the third one you add these two together, which is valid because the function calls all return number values.


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# 8, because the return statement b+c happpens before it ever reaches return 10. since b+c is a valid number value so long as numbers are passed into it as arguments, the function call evalutes to 8, which is printed. 

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#500, 500 , 300, 300 First b is assigned the value 500. then foobar() is defined, but not called, so b stays 500. then foobar() is called, and b is reassigned the value 300, and printed, and then it's printed again outside of the function. 

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# 500,500, 300, 300. adding return b really doesn't change anything. it's not printing foobar, it's printing b. 

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#500, 500, 300,  300. same thing, though what's happening is a little different. the 500s are the same. the 300 is kinda the same. it's printing within the function, but the function is being called because the value is being assigned. the last 300 is a little different because b is assigned the function call value out side of the function, which also happens to be 300. 

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#i think function definitions all occur before function calls. therefore this should be 1, 3, 2. 

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

# 1, 3, 5, 10. first, foo() is called so that the function call can be assigned to y. but, before it's assigned, it has to be evaluated. during the function evaluation, 1 is printed, and then bar() is assigned to x, and bar() has to be evaluated within the structure of foo().  in bar()'s evaluation, it prints 3, and then it returns 5, meaning x is now 5, and x is printed in foo(). but foo()'s function call evaluates to 10 because that's the return value. that's what is eventually assigned to y, which is then printed. 