#Rotate for a Max
#Codewars
#https://www.codewars.com/kata/56a4872cbb65f3a610000026/train/python

def max_rot(n):
'''
Последовательно вращает цифры числа:
на каждом шаге текущая цифра переносится в конец.
Возвращает максимальное число,
полученное в процессе вращений.
'''
    s = str(n)
    max_n = n
    for i in range(len(s)):
        s = s[:i] + s[i + 1:] + s[i]
        if int(s) > int(max_n):
            max_n = s
    return int(max_n)
