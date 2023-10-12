''' Даны две дроби A/B и C/D (А, В, С, D — натуральные числа).
Составить программу деления дроби на дробь. Ответ должен быть несократимой дробью.
Использовать подпрограмму алгоритма Евклида для определения НОД. '''
def gcd(a, b):
    while b != 0:
    a, b = b, a % b
    return a
def divide_fraction(a, b, c, d):
    numerator = a * d
    denominator = b * c
    divisor = gcd(numerator, denominator)
    return numerator, denominator
A = 3
B = 5
C = 2
D = 7
result = divide_fraction(A, B, C, D)
print("Результат деления:", result[0], "/", result[1])