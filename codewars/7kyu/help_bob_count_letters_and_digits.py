#Help Bob count letters and digits.
#Codewars
#https://www.codewars.com/kata/5738f5ea9545204cec000155/train/python

def count_letters_and_digits(s):
'''
Подсчитывает количество букв и цифр в строке.
Аргументы:
    s: входная строка
Возвращает:
    Количество символов, являющихся буквами или цифрами.
'''
    count = 0
    for c in s:
        if c.isalnum():
            count += 1
    return count
