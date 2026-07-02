# Maxie and Minnie
# Codewars
# https://www.codewars.com/kata/6a35c1e3e4e955fbc49dec03/train/python

def swap(number):
"""
Задача:
Найти максимальное и минимальное число, которое можно
получить, выполнив не более одной перестановки любых двух цифр.
Числа с ведущим нулём не допускаются.

Решение:
Число преобразуется в список цифр. С помощью двух вложенных
циклов перебираются все уникальные пары индексов. После каждой
перестановки собирается новое число, которое сравнивается с
текущими максимумом и минимумом. После проверки цифры
возвращаются на исходные позиции.

Что изучил:
- преобразование int → str → list и обратно;
- полный перебор (brute force);
- перебор всех уникальных пар индексов;
- обмен элементов списка;
- continue;
- обработку граничных случаев (ведущий ноль).
"""
    maximum = number
    minimum = number
    num_lst = list(str(number))

    for i in range(len(num_lst)):
        for y in range(i + 1, len(num_lst)):
            num_lst[i], num_lst[y] = num_lst[y], num_lst[i]
            if num_lst[0] == '0':
                num_lst[i], num_lst[y] = num_lst[y], num_lst[i]
                continue
            candidate = int(''.join(num_lst))
            if candidate > maximum:
                maximum = candidate
            if candidate < minimum:
                minimum = candidate
            num_lst[i], num_lst[y] = num_lst[y], num_lst[i]
    return maximum, minimum
