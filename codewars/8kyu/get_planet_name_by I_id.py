#Get Planet Name By ID
#Codewars
#https://www.codewars.com/kata/515e188a311df01cba000003/solutions/python

def get_planet_name(id):
  """
  Возвращает название планеты по индексу
  """
    planets = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune"
    ]
    return planets[id - 1]
