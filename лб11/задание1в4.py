'''Разработать класс, описывающий некоторый объект из заданной предметной области.
Класс должен содержать:
1)строку документации;
2)не менее 6 атрибутов (переменных);
3)не менее 4 методов, выполняющих обработку атрибутов класса.
В основной программе выполнить следующее:
1)Вывести на экран документацию класса.
2)Создать и инициализировать различными значениями пять экземпляров разработанного класса.
Предметные области: Сведения о гражданах.'''
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
    change_address(new_address): изменяет адрес проживания
    get_full_name(): возвращает полное имя гражданина
    is_adult(): проверяет, является ли гражданин совершеннолетним
    change_passport_number(new_passport_number): изменяет номер паспорта
    """
    def __str__(self):
        """Возвращает строковое представление самолета."""
        return f'имя: {self.name},' \
               f'возраст: {self.age}, адрес: {self.address}, ' \
               f'пол: {self.gender}, национальность: {self.nation}, ' \
               f'номер паспорта: {self.passport_number}'

    def __init__(self, name, age, gender, passportNumber, address, nation):#конструктор с параметрами name, age, gender, passportNumber, address, nation
        self.name = name
        self.age = age
        self.gender = gender
        self.passport_number = passportNumber
        self.address = address
        self.nation = nation#инициализируем каждый параметр
    def change_address(self, new_address):
        self.address = new_address
    def get_full_name(self):
        return self.name
    def is_adult(self):
        return self.age >= 18
    def change_passport_number(self, new_passport_number):
        self.passport_number = new_passport_number
print(Graj.__doc__)#вывод документации класса
graj1 = Graj("Емельянович Арсений", 25, "Мужской", "634634634", "ул.Борунская,д.незнаю", "белорус")
graj2 = Graj("Побединский Архип", 30, "Мужской", "65475646", "новошишки,д.нездаю", "белорус")
graj3 = Graj("Иван Мишенков", 40, "Мужской", "654645646", "г.Ошмяны,ул.Западная,д.5", "белорус")
graj4 = Graj("Тополь Алексей", 22, "Мужской", "2343423424", "г.Ошмяны, ул.Западная,д.5", "белорус")
graj5 = Graj("Алексеев Алексей", 28, "Мужской", "9789879899", "г.Ошмяны, ул.Западная,д.5", "белорус")
#информация на 5 граждан
print(graj1)
print(graj2)
print(graj3)
print(graj4)
print(graj5)