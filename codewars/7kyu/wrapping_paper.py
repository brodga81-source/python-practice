#Wrapping Paper
#Codewars
#https://www.codewars.com/kata/69ea4c6708b1c58c36ac735a/train/python
def wrapping_paper(boxes):
"""
Вычисляет общее количество упаковочной бумаги
для набора прямоугольных коробок.
Для каждой коробки учитывается площадь поверхности
и дополнительный запас, равный площади
самой маленькой стороны.
"""
    total = 0
    for  l, w, h in (boxes):
        side1 = l * w
        side2 = w * h
        side3 = h * l
        
        total += 2*side1 + 2*side2 + 2*side3 + min(side1, side2, side3)
        
    return total
