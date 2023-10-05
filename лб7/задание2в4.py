films = {'terminator': 10,'the boys': 7,'barbi': 0,'flash': 9,'legend №17': 6,'the avengers': 5,'rick and morty': 10}
#все фильмы
print(films)#вывод фильмов
for key, value in films.items():#для key, value в названиях фильмов
    print(key, value)#вывод key и value

key = input('Введите ключ: ')#key присваиваем ipnut ввод ключа
# Проверка на наличие ключа в словаре
if key in films:#если ключ есть в фильмах
    print('Значение:', films[key])#вывод значения
else:#иначе
    print('такого фильма нет')#если фильма нет вывод этого текста