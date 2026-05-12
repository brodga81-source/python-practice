#Sequence to 1
#Codewars
#https://www.codewars.com/kata/5a05fe8a06d5b6208e00010b/train/python
def seq_to_one(n):
"""
Возвращает последовательность чисел
от n до 1.
"""
    result = []
    if n >= 1:
        for c in range(n, 0, -1):
            result.append(c)
    else:
        for c in range(n, 2, 1):
            result.append(c)

    return result
