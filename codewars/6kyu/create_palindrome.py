#Create palindrome
#Codewars
#https://www.codewars.com/kata/5b7bd90ef643c4df7400015d/train/python

def solve(st):
  '''
  """
Проверка возможности получить палиндром после замены
каждой буквы на соседнюю в алфавите.

Использованы:
- ord() / chr();
- проход от краёв к центру;
- вложенные циклы;
- флаг found;
- break.
'''
    for i in range(len(st) // 2):
        left = st[i]
        right = st[-i-1]
        if left == 'a':
            left_possible = ['b']
        elif left == 'z':
            left_possible = ['y']
        else:
            left_possible = [
                chr(ord(left)-1),
                chr(ord(left) + 1)
            ]
        if right == 'a':
            right_possible = ['b']
        elif right == 'z':
            right_possible = ['y']
        else:
            right_possible = [
                chr(ord(right)-1),
                chr(ord(right) + 1)
            ]
        found = False
        for l in left_possible:
            for r in right_possible:
                if l == r:
                    found = True
                    break
            if found:
                break

        if not found:
            return False
        
    return True
