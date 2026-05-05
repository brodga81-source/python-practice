#No zeros for heroes
#Codewars
#https://www.codewars.com/kata/570a6a46455d08ff8d001002/train/python
def no_boring_zeros(n):
  '''
  Возвращает число удалив все нули в конце
  '''
    if n == 0:
        return 0

    while n % 10 == 0:
        n //= 10
    return n
