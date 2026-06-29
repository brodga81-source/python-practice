#Twice as old
#Codewars
#https://www.codewars.com/kata/5b853229cfde412a470000d0/train/python

def twice_as_old(dad_years_old, son_years_old):
  """
   Функция вычисляет, сколько лет отделяет текущий возраст отца
   от момента, когда он был или будет ровно в два раза старше сына.
  """
    x = dad_years_old - son_years_old * 2
    return abs(x)
