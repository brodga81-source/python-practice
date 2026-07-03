# Enumerable Magic #5
# Codewars
# https://www.codewars.com/kata/54599705cbae2aa60b0011a4/train/python

from typing import Iterable, Callable

def one(xs: Iterable, predicate: Callable[..., bool]) -> bool:
"""
Задача:
Проверить, возвращает ли переданная функция True
ровно для одного элемента последовательности.

Решение:
Последовательно пройти по всем элементам коллекции.
Для каждого элемента вызвать переданную функцию.
Подсчитать количество значений True и вернуть результат
проверки count == 1.

Что изучил:
- передача функции в качестве аргумента;
- вызов функции через переменную (predicate(x));
- подсчёт количества совпадений;
- возврат булевого выражения (return count == 1).
"""
    count = 0
    for x in xs:
        if predicate(x):
            count += 1
    return count == 1
