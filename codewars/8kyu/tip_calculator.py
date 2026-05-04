#Tip Calculator
#Codewars
#https://www.codewars.com/kata/56598d8076ee7a0759000087/train/python

import math


def calculate_tip(amount, rating):
  """
  Рассчитывает чаевые на основе рейтинга обслуживания.
  Возвращает округлённое вверх значение чаевых или сообщение об ошибке.
  """  
  tip = 0
    rating = rating.lower()
    if rating == 'terrible':
        tip = 0
    elif rating == 'poor':
        tip = amount * 0.05
    elif rating == 'good':
        tip = amount * 0.1
    elif rating == 'great':
        tip = amount *0.15
    elif rating == 'excellent':
        tip = amount * 0.2
    else:
        return "Rating not recognised"

    return math.ceil(tip)
