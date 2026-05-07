#Sum of Array Averages
#Codewars
#https://www.codewars.com/kata/56d5166ec87df55dbe000063/train/python

def sum_average(lists: list[list[int]]) -> float:
  '''
Вычисляет среднее значение каждого списка
и возвращает сумму всех средних значений.
  '''
    total = 0
    for arr in lists:
        total += sum(arr) / len(arr)
    return total
