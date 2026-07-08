# Complementary DNA
# Codewars
# https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python

def DNA_strand(dna):
'''
Задача:
Преобразовать цепочку ДНК в комплементарную, заменяя:
A ↔ T
C ↔ G

Решение:
Прошелся по каждому символу строки.
С помощью условий if/elif определил соответствующую замену.
Постепенно собрал новую строку и вернул результат.

Что закрепил:
- цикл for;
- работу со строками;
- построение новой строки;
- использование нескольких условий if/elif.
'''
    result = ''
    for ch in dna:
        if ch == 'A':
            result += 'T'
        elif ch == 'T':
            result += 'A'
        elif ch == 'G':
            result += 'C'
        elif ch == 'C':
            result += 'G'
    return result
