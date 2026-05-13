#The Feast of Many Beasts
#Codewars
#https://www.codewars.com/kata/5aa736a455f906981800360d/train/python
def feast(beast, dish):
    if beast[0] == dish[0] and beast[-1] == dish[-1]:
        return True
    return False
