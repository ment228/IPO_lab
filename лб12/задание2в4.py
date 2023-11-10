'''Разработать класс, описывающий некоторый объект из заданной предметной области.
Класс должен содержать:
1)строку документации;
2)не менее 6 атрибутов (переменных);
3)не менее 4 методов, выполняющих обработку атрибутов класса.
В основной программе выполнить следующее:
1)Вывести на экран документацию класса.
2)Создать и инициализировать различными значениями пять экземпляров разработанного класса.
Предметные области: Сведения о гражданах.'''
'''
Добавить в класс конструктор, выполняющий инициализацию всех или некоторых атрибутов экземпляра класса. Те атрибуты, которые инициализируются в конструкторе, удалить из описания класса.
Сделать так, чтобы инициализация атрибутов в конструкторе выполнялась с помощью сеттеров.
Создать одномерный список из 10 объектов класса (данные ввести с клавиатуры) используя конструктор.
Добавить в класс деструктор (финализатор). В теле деструктора реализовать вывод сообщения о том, что деструктор выполнился. 
'''
class Graj:#новый класс
    """
    Класс описывающий гражданина
    Атрибуты:
    name: имя гражданина
    age: возраст гражданина
    gender: пол гражданина
    passportNumber: номер паспорта
    address: адрес проживания
    nation: национальность гражданина

    Методы:
    change_address: изменяет адрес проживания
    get_full_name: возвращает полное имя гражданина
    is_adult: проверяет, является ли гражданин совершеннолетним
    change_passport_number: изменяет номер паспорта
    """
    def __str__(self):
        return f'имя: {self.name},' \
               f'возраст: {self.age}, адрес: {self.address}, ' \
               f'пол: {self.gender}, национальность: {self.nation}, ' \
               f'номер паспорта: {self.passportNumber}'#возвращает строковое представление граждан

    def __init__(self, name, age, gender, passportNumber, address, nation):#конструктор с параметрами name, age, gender, passportNumber, address, nation
        self.name = name
        self.age = age
        self.gender = gender
        self.passportNumber = passportNumber
        self.address = address
        self.nation = nation#инициализируем каждый параметр
    def set_address(self, new_address):
        self.address = new_address#устанавливает новый адрес
    def set_name(self, new_name):
        self.name = new_name#устанавливает новое имя
    def set_age(self, new_age):
        return new_age if new_age >= 18 else 0#устанавливает новый возраст если 18 и больше иначе 0
    def set_passport_number(self, new_passport_number):
        self.passportNumber = new_passport_number#устанавливает новый номер паспорта
    def set_gender(self, new_gender):
        self.gender = new_gender#устанавливает новый пол
    def set_nation(self, new_nation):
        self.nation = new_nation#устанавливает новую национальность
    def change_address(self, new_address):
        self.set_address(new_address)#изменяет адрес
    def get_full_name(self):
        return self.name#возвращает полное имя
    def is_adult(self):
        return self.age >= 18#проверка возраста
    def change_passport_number(self, new_passport_number):
        self.set_passport_number(new_passport_number)#изменяет номер паспорта
    def __del__(self):
        print("Деструктор выполнился.")#вывод сообщения что деконструктор выполнился
# Создание списка из 10 объектов класса, данные вводятся с клавиатуры
citizens = []
for _ in range(10):
    name = input("Введите имя гражданина: ")
    age = int(input("Введите возраст гражданина: "))
    gender = input("Введите пол гражданина: ")
    passportNumber = input("Введите номер паспорта: ")
    address = input("Введите адрес проживания: ")
    nation = input("Введите национальность гражданина: ")

    citizen = Graj(name, age, gender, passportNumber, address, nation)
    citizens.append(citizen)

# Вывод информации о всех гражданах
for citizen in citizens:
    print(citizen)