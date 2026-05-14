#How good are you really?
#Codewars
#https://www.codewars.com/kata/5601409514fc93442500010b/train/python

def better_than_average(class_points, your_points):
"""
Проверяет, превышает ли результат пользователя
средний балл класса.
"""
    if sum(class_points) / len(class_points) < your_points:
        return True
    return False
