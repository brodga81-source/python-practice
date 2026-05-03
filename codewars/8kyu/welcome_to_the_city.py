#Welcome to the City
#Codewars
#https://www.codewars.com/kata/5302d846be2a9189af0001e4/solutions/python

def say_hello(name, city, state):
  '''
  Возвращает строку приветствия.
    Аргументы:
        name: список частей имени (например, ['John', 'Smith'])
        city: название города
        state: название штата
    Возвращает:
        Отформатированную строку приветствия.
    '''
    full_name = ' '.join(name)
    return f"Hello, {full_name}! Welcome to {city}, {state}!"
