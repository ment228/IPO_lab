'''Введите с клавиатуры N целых чисел (N также вводится с клавиатуры и запишите их в
текстовый файл file1_NN.txt.

Вариант 4. Запишите в другой текстовый файл file2_NN.txt только нечетные числа из первого файла.
'''

N = int(input("Введите количество чисел: "))#запрашиваем пользователя ввести колво чисел
numbers = []#создаем список для чисел
for i in range(N):#цикл для i до N
    number = int(input("Введите число: "))#запрашиваем пользователя ввести N чисел
    numbers.append(number)#добавляет числа в список
with open("file1_NN.txt", "w") as file:#открываем файл для записи
    for number in numbers:#
        file.write(str(number) + "\n")#Запишем информацию в файл hello.txt
with open("file2_NN.txt", "w") as file:#открываем файл для записи
    for number in numbers:#
        if number % 2 != 0:#
            file.write(str(number) + "\n")#нечетные числа Запишем информацию в файл hello.txt
