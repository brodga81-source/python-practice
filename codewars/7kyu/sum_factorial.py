#Sum Factorial
#Codewars
#https://www.codewars.com/kata/56b0f6243196b9d42d000034/train/python

def factorial(n):
'''
Вычисляет факториал числа
'''
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result

def sum_factorial(lst):
'''
Возвращает сумму факториалов всех чисел в списке
'''
    total = 0
    for i in lst:
        total += factorial(i)
    return  total
