#Simple Fun #74: Growing Plant
#Codewars
#https://www.codewars.com/kata/58941fec8afa3618c9000184/train/python
def growing_plant(up_speed, down_speed, desired_height):
"""
Симулирует рост растения по дням
и возвращает количество дней,
необходимое для достижения нужной высоты.
"""
    plant_height = 0
    count_day = 0
    while True:
        plant_height += up_speed
        count_day +=1
        if plant_height >= desired_height:
            return count_day
        plant_height -= down_speed
