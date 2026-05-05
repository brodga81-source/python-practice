#Ordered Count of Characters
#Codewars
#https://www.codewars.com/kata/57a6633153ba33189e000074/train/python

def ordered_count(s): #abc
  '''
  Подсчитывает количество вхождений каждого символа в строке
  и возвращает список кортежей (символ, количество)
  в порядке их первого появления.
  '''
    counts = {}
    for c in s:
        if c in counts:
            counts[c] +=1
        else:
            counts[c] = 1
    return  list(counts.items())
