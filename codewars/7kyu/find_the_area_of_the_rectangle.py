#Find the area of the rectangle!
#Codewars
#https://www.codewars.com/kata/580a0347430590220e000091/train/python

def area(d, l):
"""
Вычисляет площадь прямоугольника
по диагонали и одной стороне.

Если диагональ меньше или равна стороне,
возвращает "Not a rectangle".
"""
    if d <= l:
        return "Not a rectangle"
    b = (d**2 - l**2) ** 0.5
    return l * b
