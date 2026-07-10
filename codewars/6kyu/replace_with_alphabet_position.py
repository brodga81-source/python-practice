# Replace With Alphabet Position
# Codewars
# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python

def alphabet_position(text):
'''
Задача:
Заменить каждую букву текста её позицией в английском алфавите, игнорируя регистр и все посторонние символы.

Решение:
Создал строку английского алфавита.
Привёл входной текст к нижнему регистру.
Прошёл циклом по каждому символу текста.
Проверил наличие символа в алфавите.
С помощью метода index() получил индекс буквы и прибавил 1.
Преобразовал полученную позицию в строку и добавил в список.
Объединил позиции букв через пробел методом join().

Что закрепил:
- метод lower();
- проверку принадлежности через оператор in;
- метод index();
- преобразование int в str;
- накопление результата в списке;
- объединение элементов через join().
'''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    text_low = text.lower()
    for ch in text_low:
        if ch in alphabet:
            result.append(str(alphabet.index(ch) + 1))
    return ' '.join(result)
