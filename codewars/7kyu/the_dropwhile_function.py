#The dropWhile Function
#Codewars
#https://www.codewars.com/kata/54f9c37106098647f400080a/train/python

def drop_while(arr, pred):
"""
Удаляет элементы из начала списка,
пока условие pred возвращает True.
"""
    for index, c in enumerate(arr):
        if not pred(c):
            return arr[index:]
    return []
