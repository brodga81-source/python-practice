# Who likes it?
# Codewars
# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python

def likes(names):
'''
Задача:
Сформировать текст о количестве лайков в зависимости от числа пользователей.

Решение:
Проверил количество имён с помощью условной конструкции if-elif-else.
Для пустого списка вернул сообщение об отсутствии лайков.
Для одного, двух и трёх пользователей сформировал отдельные строки с их именами.
Для четырёх и более пользователей вывел первые два имени и вычислил количество остальных через len(names) - 2.
Использовал f-строки для подстановки имён и значений.

Что закрепил:
- проверку пустого списка через not;
- конструкцию if-elif-else;
- получение элементов списка по индексам;
- функцию len();
- форматирование текста с помощью f-строк;
- выбор разного результата в зависимости от количества элементов.
'''
    if not names:
        return 'no one likes this'
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'
