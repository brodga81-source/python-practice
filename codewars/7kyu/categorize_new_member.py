# Categorize New Member
# Codewars
# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python

def open_or_senior(data):
"""
Определяет категорию участников клуба
на основе возраста и гандикапа.
Возвращает список категорий:
"Senior" или "Open".
"""
    result = []
    for age, handicap in data:
        if age >= 55 and handicap > 7:
            result.append('Senior')
        else:
            result.append('Open')
    return result
