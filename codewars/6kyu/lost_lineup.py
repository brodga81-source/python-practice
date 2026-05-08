#Lost Lineup
#Codewars
#https://www.codewars.com/kata/6914c975e159c8f7e120cc84/train/python?collection=7kyu-to-train

def find_lineup(distances):
"""
Восстанавливает порядок людей в очереди
по их воспоминаниям о количестве людей
между ними и Кэррол.
Возвращает пустой список,
если восстановить очередь невозможно.
"""
    result = [0] * len(distances)
    for person, position in enumerate(distances, start=1):
        if position >= len(distances):
            return []
        if result[position] != 0:
            return []
        result[position] = person
    return result
