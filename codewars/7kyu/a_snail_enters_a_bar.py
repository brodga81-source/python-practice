# A snail enters a bar
# Codewars
# https://www.codewars.com/kata/66cdc6ab9e7a9f009e0ca8f6/train/python

def can_snail_reach_end(length, speed, length_increases):
  """
Задача:
Определить, сможет ли улитка доползти до конца
растягивающейся резинки за один год.

Решение:
Смоделировал процесс по минутам.
На каждой итерации увеличивал длину резинки и
смещал улитку вперед.
Если улитка достигала конца — возвращал True.
После окончания симуляции возвращал False.

Что изучил:
- моделирование процессов;
- использование цикла for для симуляции времени;
- ранний выход из функции;
- оптимизацию через предварительную проверку
  невозможного случая (speed <= length_increases).
"""
    snail_position = 0
    if speed <= length_increases:
        return False
    for i in range(525600):
        length += length_increases
        snail_position += speed
        if snail_position >= length:
            return True
    return False
