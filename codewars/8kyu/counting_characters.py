#Counting Characters
#Codewars
#https://www.codewars.com/kata/55f1b763dd670651620000ce/train/python

def count_char_occurrences(strng, char):
  '''
  возвращает кол-во указанных символов в строке
  '''
    count = 0
    for i in strng:
        if i == char:
            count += 1
    return count
