#Calculate mean and concatenate string
#Codewars
#https://www.codewars.com/kata/56f7493f5d7c12d1690000b6/train/python

messege = ['u', '6', 'd', '1', 'i', 'w', '6', 's', 't', '4', 'a', '6', 'g', '1', '2', 'w', '8', 'o', '2', '0']
def mean(lst):
    '''
    Возвращает среднее значение цифр и строку из символов.
    '''
    total = 0
    total_char = []
    for char in lst:
        if char.isdigit():
            total += int(char)
        else:
            total_char.append(char)
    total /= 10
    return [total, ''.join(total_char)]
