name_list = ['daniil','alexey','artem','nikita','ivan','vlad','IGOR']#список имен
name_tuple = tuple(name_list)#из списка в кортеж
print(name_tuple)#вывод
new_tu = tuple(name_list[0:3])#из списка в кортеж
print(new_tu)#вывод
new_tu2 = tuple(name_list[3:7])#из списка в кортеж
print(new_tu2)#вывод
all_tu1 = [tuple(name_list), name_tuple, new_tu, new_tu2]#присваиваем all_tu все (tuple(name_list) из списка в кортеж)
all_tu = tuple(all_tu1)#из списка в кортеж
print(all_tu)#вывод всего