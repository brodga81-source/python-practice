#Training JS #32: methods of Math---round() ceil() and floor()
#Codewars
#https://www.codewars.com/kata/5732d3c9791aafb0e4001236/train/python

import math

def round_it(n):
    left, right = str(n).split('.')
    if len(left) < len(right):
        return math.ceil(n)
    elif len(left) > len(right):
        return math.floor(n)
    return round(n)
