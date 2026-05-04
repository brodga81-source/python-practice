#Grasshopper - Summation
#Codewars
#https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python
def summation(num):
    '''
    Возвращает сумму чисел от 1 до num
    '''
    count = 0
    for i in range(num + 1):
        count += i
    return count
