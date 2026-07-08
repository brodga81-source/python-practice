# You're a square
# Codewars
# https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python

import math


def is_square(n):
'''
Задача:
Определить, является ли заданное число идеальным квадратом.

Решение:
Сначала обработал отрицательные числа, сразу возвращая False.
Для остальных чисел вычислил квадратный корень с помощью math.sqrt().
Проверил, является ли результат целым числом, используя метод is_integer().

Что изучил:
- math.sqrt();
- метод is_integer();
- ранний выход из функции (early return);
- упрощение условий, когда выражение уже возвращает True или False.
'''
    if n < 0:
        return False
    return math.sqrt(n).is_integer()
