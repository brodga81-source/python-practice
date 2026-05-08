#Simple Fun #87: Shuffled Array
#Codewars
#https://www.codewars.com/kata/589573e3f0902e8919000109/train/python

shuffled = [1, 12, 3, 6, 2]

def shuffled_array(s):
"""
Находит число, являющееся суммой остальных элементов,
удаляет его и возвращает отсортированный массив.
"""
    total = 0
    for i in s:
        if i == sum(s) / 2:
            total = i
    s.remove(total)
    return sorted(s)
