#Mythical Heads and Tails
#Codewars
#https://www.codewars.com/kata/5751aa92f2dac7695d000fb0/solutions/python

def beasts(heads, tails):
"""
Вычисляет количество Orthrus и Hydra
по общему количеству голов и хвостов.
Возвращает список:
[orthrus, hydra]
Если решения не существует,
возвращает "No solutions".
"""
    extra_heads = heads - tails * 2
    hydra = extra_heads // 3
    orthrus = tails - hydra
    if extra_heads % 3 == 0 and hydra >= 0 and orthrus >= 0:
        return [orthrus, hydra]
    else:
        return "No solutions"
