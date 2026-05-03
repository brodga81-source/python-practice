#Get the mean of an array
#Codewars
#https://www.codewars.com/kata/563e320cee5dddcf77000158/train/python?collection=easy-8-kyu

def get_average(marks):
    """
    Возвращает среднее значение списка чисел, округлённое вниз до целого.
    """
    return sum(marks) // len(marks)
