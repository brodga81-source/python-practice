def zero (operation = None):
    if operation is None:
        return 0
    else:
        return operation(0)

def one(operation = None):
    if operation is None:
        return 1
    else:
        return operation(1)

def two(operation = None):
    if operation is None:
        return 2
    else:
        return operation(2)

def three(operation = None):
    if operation is None:
        return 3
    else:
        return operation(3)

def four(operation = None):
    if operation is None:
        return 4
    else:
        return operation(4)

def five(operation = None):
    if operation is None:
        return 5
    else:
        return operation(5)

def six(operation = None):
    if operation is None:
        return 6
    else:
        return operation(6)

def seven(operation = None):
    if operation is None:
        return 7
    else:
        return operation(7)

def eight(operation = None):
    if operation is None:
        return 8
    else:
        return operation(8)

def nine(operation = None):
    if operation is None:
        return 9
    else:
        return operation(9)

def times(right_number):
    def operation(left_number):
        return left_number * right_number
    return operation

def plus(right_number):
    def operation(left_number):
        return left_number + right_number
    return operation

def minus(right_number):
    def operation(left_number):
        return left_number - right_number
    return operation

def divided_by(right_number):
    def operation(left_number):
        return left_number // right_number
    return operation
'''
Задача:
Реализовать вычисления с помощью функций для чисел от 0 до 9 и математических операций: сложения, вычитания, умножения и целочисленного деления.

Примеры:
seven(times(five())) → 35
four(plus(nine())) → 13
eight(minus(three())) → 5
six(divided_by(two())) → 3

Решение:
Создал отдельную функцию для каждого числа от zero() до nine().

Каждая числовая функция работает в двух режимах:
- если операция не передана, возвращает своё числовое значение;
- если операция передана, вызывает полученную функцию и передаёт ей своё число как левый операнд.

Каждая математическая функция принимает правый операнд, создаёт внутреннюю функцию operation() и возвращает её.

Внутренняя функция:
- запоминает правый операнд благодаря замыканию;
- позже получает левый операнд от внешней числовой функции;
- выполняет необходимое вычисление.

Например:
five() возвращает 5.
times(5) создаёт и возвращает функцию «умножить на 5».
seven() получает эту функцию и вызывает её, передавая число 7.
В результате вычисляется 7 * 5 = 35.

Что изучил и закрепил:
- порядок выполнения вложенных функций;
- функции как объекты;
- передачу функции в качестве аргумента;
- возврат функции из другой функции;
- создание вложенных функций;
- отличие между возвратом функции и её вызовом;
- работу замыканий;
- использование необязательных аргументов;
- целочисленное деление с помощью //.'''



print(seven(times(five())))
print(four(plus(nine())))
print(eight(minus(three())))
print(six(divided_by(two())))
