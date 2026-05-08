#Finish Guess the Number Game
#Codewars
#https://www.codewars.com/kata/568018a64f35f0c613000054/train/python

class Guesser:
  """
  Класс игры-угадайки с ограниченным количеством попыток.
- Возвращает True при правильном ответе
- Уменьшает lives при ошибке
- Вызывает ошибку при отсутствии жизней
  """
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives

    def guess(self, n):
        if self.lives <= 0:
            raise ValueError
        if n == self.number:
            return True
        else:
            self.lives -= 1
            return False
