#How Many Lonely Letters?
#Codewars
#https://www.codewars.com/kata/69cda5b85599f307742ce70a/train/python

def count_lonely_letters(text):
    """
    Подсчитывает количество одиноких букв в строке.
    Буква считается одинокой,
    если встречается один раз
    и не имеет соседей по алфавиту в строке.
    """
    s = text.lower()
    count = 0
    for c in s:
        if c.isalpha() and s.count(c) == 1:
            left = chr(ord(c)-1)
            right = chr(ord(c)+1)
            if c == 'a':
                if right not in s:
                    count+=1
            elif c == 'z':
                if left not in s:
                    count+=1
            else:
                if left not in s and right not in s:
                    count +=1
    return count


