# noobCode 03
# Codewars
# https://www.codewars.com/kata/57470efebf81fea166001627/train/python

def letter_check(string_pair: list[str]) -> bool:
"""
Задача:
Проверить, присутствуют ли все символы второй строки
в первой строке без учета регистра.

Решение:
Обе строки приводятся к нижнему регистру.
Для каждой буквы второй строки проверяется её наличие
в первой строке. Если хотя бы одной буквы нет —
сразу возвращается False. Если проверка успешно
завершилась, возвращается True.

Что изучил:
- метод lower();
- распаковку списка (first, second = string_pair);
- оператор in / not in;
- ранний выход из функции (return False);
- упрощение алгоритма с помощью встроенных возможностей Python.
"""
    first, second = string_pair
    first = first.lower()
    second = second.lower()
    for i in second:
        if i not in first:
            return False
    return True
