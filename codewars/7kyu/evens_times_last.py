#Evens times last
#Codewars
#https://www.codewars.com/kata/5a1a9e5032b8b98477000004/train/python
def even_last(numbers):
"""
Считает сумму элементов с чётными индексами
и умножает её на последний элемент списка.
Если список пуст, возвращает 0.
"""
    sum_even = 0
    if numbers == []:
        return 0
    for i in range(len(numbers)):
        if i % 2 == 0:
            sum_even += numbers[i]
    sum_even = sum_even * numbers[-1]

    return sum_even
