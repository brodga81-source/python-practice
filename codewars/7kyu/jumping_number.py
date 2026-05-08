#Jumping Number
#Codewars
#https://www.codewars.com/kata/5a54e796b3bfa8932c0000ed/train/python

def jumping_number(number):
    """
    Проверяет, отличается ли каждая соседняя цифра числа на 1.
    Возвращает "Jumping!!", если число является jumping number,
    иначе возвращает "Not!!".
    """
    number = str(number)
    for c in range(len(number)-1):
        if abs(int(number[c]) - int(number[c + 1])) != 1:
            return 'Not!!'
    return 'Jumping!!'
