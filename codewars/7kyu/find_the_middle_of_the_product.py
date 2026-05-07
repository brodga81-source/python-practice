#Find the Middle of the Product
#Codewars
#https://www.codewars.com/kata/5ac54bcbb925d9b437000001/train/python

def find_middle(st):
'''
Находит произведение всех цифр в строке
и возвращает среднюю цифру результата.
Если количество цифр в результате чётное,
возвращает две средние цифры как число.
'''
    total = []
    result = 1

    if not isinstance(st, str):
        return -1

    for char in st:
        if char.isdigit():
            total.append(int(char))

    if not total:
        return -1

    for i in total:
        result *= i
    s = str(result)
    if len(s) % 2 == 0:
        middle = len(s) // 2
        return int(s[middle - 1: middle + 1])
    else:
        return int(s[len(s) // 2])
