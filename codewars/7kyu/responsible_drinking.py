# Responsible Drinking
# Codewars
# https://www.codewars.com/kata/5aee86c5783bb432cd000018/train/python

def hydrate(drink_string):
"""
Задача:
Подсчитать количество напитков, указанных в строке,
и вернуть рекомендацию по количеству стаканов воды.

Решение:
Прошел по строке посимвольно.
Если символ является цифрой, прибавил его к счетчику.
После подсчета сформировал строку с учетом
единственного и множественного числа.

Что изучил:
- метод isdigit();
- преобразование символа в число через int();
- проход по строке циклом;
- использование f-строк.
"""
    count = 0
    for ch in drink_string:
        if ch.isdigit():
            count += int(ch)
    if count == 1:
        return "1 glass of water"
    return f'{count} glasses of water'
