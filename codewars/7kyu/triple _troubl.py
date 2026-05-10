#Triple Trouble
#Codewars
#https://www.codewars.com/kata/5704aea738428f4d30000914/train/python

def triple_trouble(one, two, three):
"""
Объединяет символы трёх строк по индексам
и возвращает новую строку.
"""
    result = ' '
    for i in range(len(one)):
        result += one[i] + two[i] + three[i]
    return result
