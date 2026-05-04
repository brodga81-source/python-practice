#Job Matching #1
#Codewars
#https://www.codewars.com/kata/56c22c5ae8b139416c00175d/train/python

def job_matching(candidate, job):
    '''
    Проверяет, подходит ли вакансия кандидату по зарплатным ожиданиям.
    Учитывается 10% гибкость кандидата (снижение минимальной зарплаты).
    Args:
        candidate: словарь с ключом 'min_salary'
        job: словарь с ключом 'max_salary'
    Returns:
        True, если вакансия подходит, иначе False
    Raises:
        ValueError: если отсутствуют необходимые ключи
    '''
    if 'min_salary' not in candidate:
        raise ValueError("'min_salary' not in candidate")
    if 'max_salary' not in job:
        raise ValueError("'max_salary' not in job")
    return candidate['min_salary'] * 0.9 <= job['max_salary']
