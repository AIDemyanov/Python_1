# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]

new_list = int(input('Введите новый элемент рейтинга - '))
count = my_list.count(new_list)

for el in my_list:
    if count > 0:
        index = my_list.index(new_list)
        my_list.insert(count + index, new_list)
        break
    elif new_list > el:
        index_2 = my_list.index(el)
        my_list.insert(index_2, new_list)
        break
    else:
        my_list.append(new_list)
        break

print(my_list)
