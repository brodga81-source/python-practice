# Password entropy
# Codewars
# https://www.codewars.com/kata/6a1f03fac18f58f98ad9d21a/train/python

import math

def entropy(password):
Задача:
Рассчитать энтропию пароля по формуле E = L × log₂(R),
где R зависит от набора используемых символов.

Решение:
Прошел по каждому символу пароля, определил,
используются ли строчные буквы, заглавные,
цифры и специальные символы.
На основе этого вычислил размер пула символов,
после чего рассчитал энтропию с помощью math.log2().

Что изучил:
- методы строк: islower(), isupper(), isdigit();
- разницу между if и elif;
- использование модуля math и функции log2();
- разбиение задачи на этапы (сначала определить R, затем вычислить результат).
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    r = 0
    for ch in password:
        if ch.islower():
            has_lower = True
        elif ch.isupper():
            has_upper = True
        elif ch.isdigit():
            has_digit = True
        else:
            has_special = True
    if has_lower:
        r += 26
    if has_upper:
        r += 26
    if has_digit:
        r += 10
    if has_special:
        r += 32

    return len(password) * math.log2(r)
