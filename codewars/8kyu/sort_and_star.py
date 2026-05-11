# Sort and Star
# Codewars
# https://www.codewars.com/kata/57cfdf34902f6ba3d300001e/train/python

def two_sort(array):
"""
Возвращает первую строку
из отсортированного списка,
объединяя символы через "***".
"""
    arr = sorted(array)[0]
    return '***'.join(arr)
