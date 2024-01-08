#countdown
def countdown(num):
    for x in range(num, -1, -1):
        print(x)
countdown(5)

#print and return
def print_and_return (num1, num2):
    print(num1)
    return(num2)
x = print_and_return(2,5)
print(x)
#first plus length
def first_plus_length (list):
    sum= list[0] + len(list)
    return sum
my_list = [2,5,8,19,20]
z = first_plus_length(my_list)
print(z)

#values greater than second 
def values_greater_than_second(list):
    new_list =[] 
    for x in range(0, len(list)):
        if list[x] > list[1]:
            new_list.append(list[x])
    return new_list
sample = [2, 100, 101, 105, 19, 99, 5000]
print (values_greater_than_second(sample))


#this length, that value 
def size_and_value(size, value):
    list = [value] *size 
    return list
sav = size_and_value(5,10)
print(sav)