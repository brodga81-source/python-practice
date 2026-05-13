#Circles in Polygons
#Codewars
#https://www.codewars.com/kata/5a026a9cffe75fbace00007f/train/python

import math

def circle_diameter(sides, side_length):
    """
    Вычисляет диаметр наибольшего круга,
    который может поместиться
    внутри правильного многоугольника.
    """
    diameter = side_length / math.tan(math.pi / sides)
    return round(diameter, 3)
