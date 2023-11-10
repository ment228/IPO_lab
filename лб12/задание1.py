'''
1) Описать класс с именем STUDENT, содержащий следующие поля:
фамилия и инициалы;
номер группы;
успеваемость (массив из пяти элементов).

2) Написать программу, выполняющую следующие действия
ввод с клавиатуры данных в массив, состоящий из десяти структур типа STUDENT;
вывод на дисплей фамилий и номеров групп для всех студентов, имеющих хотя бы одну неудовлетворительную отметку;
если таких студентов нет, вывести соответствующее сообщение.
'''
class Students:#новый класс Students
    def __init__(self, name, group, otmetki):#конструктор с параметрами name, group, otmetki
        self.name = name
        self.group = group
        self.otmetki = otmetki#инициализируем параметры
    def plohie_otmetki(self):#
        for grade in self.otmetki:
            if grade < 4: #если отметка меньше 4 то она считается прохой
                return True#возвращаем рпавду
        return False#возвращаем ложь
studentss = []#Создаем массив из десяти структур типа Students
for i in range(10):
    name = input("введите фамилию и инициалы студента: ")
    group = input("введите номер группы: ")
    otmetki = [int(input(f"введите оценку {i + 1}: ")) for i in range(5)]
    studentss.append(Students(name, group, otmetki))
# Выводим фамилии и номера групп студентов с хотя бы одной неудовлетворительной отметкой
naideni_plohie_otmetki = False
for student in studentss:
    if student.plohie_otmetki():
        print(f"студент {student.name} из группы {student.group} имеет неудовлетворительные отметки.")#вывод учащегося с плохими отметками
        naideni_plohie_otmetki = True
if not naideni_plohie_otmetki:
    print("у всех студентов хорошая успеваемость")#вывод сообщения если у всех учащихся хорошие отметки