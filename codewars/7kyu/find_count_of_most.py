# Find Count of Most Frequent Item in an Array
# Codewars
# https://www.codewars.com/kata/56582133c932d8239900002e/train/python

def most_frequent_item_count(collection):
  """
Задача:
Найти количество вхождений наиболее часто встречающегося
элемента массива.

Решение:
Для каждого элемента подсчитывается количество его
вхождений с помощью метода count(). Максимальное
найденное значение сохраняется и возвращается после
завершения цикла.

Что изучил:
- метод list.count();
- поиск максимального значения через переменную;
- обработку пустого списка;
- питоновскую проверку `if not collection`.
"""
    max_count = 0
    if not collection :
        return 0
    for i in collection:
        count = collection.count(i)
        if count > max_count:
            max_count = count
    return max_count

