# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

dict = {'key_1' : 'Зима',
        'key_2' : 'Весна',
        'key_3' : 'Лето',
        'key_4' : 'Осень'}

list = ['Зима', 'Весна', 'Лето', 'Осень']

month = int(input('Введите месяц в виде целого числа от 1 до 12 - '))

if month == 12 or month == 1 or month == 2:
    print(dict.get('key_1'))
    print(list[0])

elif month == 3 or month == 4 or month == 5:
    print(dict.get('key_2'))
    print(list[1])

elif month == 6 or month == 7 or month == 8:
    print(dict.get('key_3'))
    print(list[2])

elif month == 9 or month == 10 or month == 11:
    print(dict.get('key_4'))
    print(list[3])

else:
    print('Такого месяца не существует!')
