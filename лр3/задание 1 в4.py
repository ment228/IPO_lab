x=int(input('введите значение a:'))
summ = 0
count = 0
for i in range(x, 201):
    summ += i
    count += 1
ar = summ/count
print('среднее арифметическое равно',ar)