#Add Length
#Codewars
#https://www.codewars.com/kata/559d2284b5bb6799e9000047/train/python
def add_length(str_):
    '''
    Возвращает список, где к каждому слову добавлена его длина
    '''
    words = str_.split()
    count = 0
    new_str = []
    for word in words:
        count = len(word)
        new_str.append(word + " " + str(count))
    return new_str
