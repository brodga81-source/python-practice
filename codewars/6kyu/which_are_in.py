def in_array(array1, array2):
    '''
    Codewars: Which are in?

Задача:
Написать функцию, которая возвращает отсортированный список строк из первого массива, являющихся подстроками хотя бы одной строки из второго массива.

Решение:
- Для каждой строки из первого массива выполняется поиск совпадения во втором массиве.
- При обнаружении подстроки строка добавляется в результирующий список.
- Используется `break` для прекращения дальнейшего поиска после первого совпадения.
- Перед возвратом результат сортируется в лексикографическом порядке.
    '''
    result = []
    for word in array1:
        for word_two in array2:
            if word in word_two:
                if word not in result:
                    result.append(word)
                break
    return sorted(result)

print(in_array(["arp", "live", "strong"],  ["lively", "alive", "harp", "sharp", "armstrong"]))



