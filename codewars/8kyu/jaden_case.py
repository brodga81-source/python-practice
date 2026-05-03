# Task: Jaden Casing Strings
# Source: Codewars
# Link: https://www.codewars.com/kata/5390bac347d09b7da40006f6

def to_jaden_case(string):
    quot = string.split()
    empty_lst = []
    for word in quot:
        empty_lst.append(word.capitalize())

    return ' '.join(empty_lst)

