import math
num1 = 5
expected1 = 15


num2 = 2.5
expected2 = 3

num3 = -1


def recursiveSigma(num):
    num = math.floor(num)
    if(num<=0):
        return 0
    else:
        return num +recursiveSigma(num-1)

print(recursiveSigma(num1))
print(recursiveSigma(num2))
print(recursiveSigma(num3))

