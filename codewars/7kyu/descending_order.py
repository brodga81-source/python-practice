# Descending Order
# Codewars
# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python

def descending_order(num):
'''
Задача:
Дано неотрицательное целое число.
Необходимо переставить его цифры в порядке убывания, чтобы получить максимально возможное число.

Решение:
Преобразовал число в строку.
Отсортировал цифры по убыванию с помощью sorted(reverse=True).
Объединил отсортированные символы в строку методом join().
Преобразовал результат обратно в целое число.

Что изучил:
- функцию sorted();
- параметр reverse=True;
- метод join();
- преобразование между int, str и списком символов.
'''
    n = str(num)
    result = sorted(n, reverse= True)
    return int(''.join(result))
