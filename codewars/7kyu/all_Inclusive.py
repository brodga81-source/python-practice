#All Inclusive?
#Codewars
#https://www.codewars.com/kata/5700c9acc1555755be00027e/train/python
def contain_all_rots(strng, arr):
"""
Проверяет, содержатся ли все циклические
повороты строки в массиве строк.
"""
    current = strng
    for i in range(len(strng)):
        if current not in arr:
            return False
        current = current[1:] + current[0]
    return True
