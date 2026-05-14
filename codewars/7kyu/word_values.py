#Word values
#Codewars
#https://www.codewars.com/kata/598d91785d4ce3ec4f000018/train/python

def name_value(my_list):
"""
Вычисляет значение каждой строки
на основе позиций букв в алфавите
и умножает его на позицию строки в списке.
"""
    result = []
    for index, word in enumerate(my_list, start=1):
        total = 0
        for c in word:
            if c !=' ':
                total += ord(c) - 96
        total *= index
        result.append(total)
    return result
