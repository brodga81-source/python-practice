# Task: Jaden Casing Strings
# Source: Codewars
# Link: https://www.codewars.com/kata/5390bac347d09b7da40006f6

def to_jaden_case(string: str) -> str:
    """
    Преобразует строку так, чтобы каждое слово начиналось с заглавной буквы.
    """
    return ' '.join(word.capitalize() for word in string.split())
if __name__ == "__main__":
    example = "how can mirrors be real if our eyes aren't real"
    print(to_jaden_case(example))
