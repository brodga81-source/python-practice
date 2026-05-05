#Ordered Count of Characters
#Codewars
#https://www.codewars.com/kata/57a6633153ba33189e000074/train/python

def ordered_count(s): #abc
  '''
  Возвращает кол-во каждого символа в строке
  '''
    counts = {}
    for c in s:
        if c in counts:
            counts[c] +=1
        else:
            counts[c] = 1
    return  list(counts.items())
