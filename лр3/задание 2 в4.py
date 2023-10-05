import math as m
#import random as r
n = int(input('введите любые числа(отрицательные в конце) через enter:'))
count = 0
while n > 0:
    count += n > 0
    n = int(input(' '))
print(count)