# if..else and ternary operat
#Codewars
#https://www.codewars.com/kata/57202aefe8d6c514300001fd/train/python
def sale_hotdogs(n):
    price = 0
    if n < 5:
        price = 100
    elif n >= 5 and n < 10:
        price = 95
    else:
        price = 90
    return price * n
