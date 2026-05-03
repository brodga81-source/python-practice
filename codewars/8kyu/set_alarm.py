# Task: Set Alarm
# Source: Codewars
#Link: https://www.codewars.com/kata/568dcc3c7f12767a62000038
def set_alarm(employed: bool, vacation: bool) -> bool:
    """
    Возвращает True, если нужно ставить будильник:
    когда человек работает и не находится в отпуске.
    """
    return employed and not vacation
if __name__ == "__main__":
    print(set_alarm(True, False))
