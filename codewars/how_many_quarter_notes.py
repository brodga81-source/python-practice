#Music 1: How Many Quarter Notes?
#Codewars
#https://www.codewars.com/kata/69c2f04a1294ffc95c526d9e/train/python
def find_quarter_notes(time_signature):
    """
    Вычисляет количество четвертных нот,
    которые помещаются в такт.
    """
    top, bottom = time_signature.split("/")
    if int(bottom) not in [1, 2, 4, 8, 16, 32, 64, 128]:
        return None
    result = int(int(top) * 4 / int(bottom))
    return result if result >= 1 else 0
