# Suzuki needs help lining up his students!
# Codewars
# https://www.codewars.com/kata/5701800886306a876a001031/train/python

def lineup_students(st):
    '''
  Задача:
    Отсортировать имена по убыванию длины.
    Если длина одинаковая — расположить их
    в обратном алфавитном порядке.

    Решение:
    Сначала список сортируется в обратном
    алфавитном порядке. Затем выполняется
    сортировка по длине в обратном порядке.
    Благодаря стабильности сортировки Python
    элементы одинаковой длины сохраняют
    порядок, полученный после первой сортировки.
    '''
    st = st.split()
    st.sort(reverse=True)
    st.sort(key = len, reverse=True)
    return st
