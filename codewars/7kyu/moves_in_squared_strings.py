#Moves in squared strings (I)
#Codewars
#https://www.codewars.com/kata/56dbe0e313c2f63be4000b25/train/python

def vert_mirror(s):
    """
    Переворачивает символы
    в каждой строке квадратной строки.
    """
    lines = s.split('\n')
    total = []
    for obj in lines:
        total.append(obj[::-1])
    return '\n'.join(total)


def hor_mirror(s):
    """
    Переворачивает порядок строк
    в квадратной строке.
    """
    lines = s.split('\n')
    return '\n'.join((lines[::-1]))


def oper(fct, s):
    """
    Применяет переданную функцию
    к строке и возвращает результат.
    """
    return fct(s)
