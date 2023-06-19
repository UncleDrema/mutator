"""
Фитнес-функция для генетического алгоритма для отбора программ на StackLang
Оценивает программу на соответствие выходным данным
Возврат - число от 0 до 1, где 1 - идеальное соответствие
"""
import copy
import math
from src.mutator import mutator
from src.language import runner
from src.converter import from_str


# Дополнение списка нулями до одинаковой длины
def fill_results(result, expected):
    if len(result) < len(expected):
        result += [0] * (len(expected) - len(result))
    elif len(result) > len(expected):
        expected += [0] * (len(result) - len(expected))


def get_metrics(program, expected):
    metrics = {
        'error': 0,
        'distance': 0,
        'length': 0,
        'diff': 0
    }
    expected = copy.copy(expected)
    result = runner.run(program)
    if result is None:
        metrics['error'] = 1
        return metrics
    diff = abs(len(result) - len(expected))
    metrics['diff'] = diff
    # Сначала дополним их нулями до одинаковой длины
    fill_results(result, expected)
    # Теперь считаем расстояние
    distance = 0
    for i in range(len(result)):
        difference = abs(result[i] - expected[i])
        if difference > 0:
            difference = max(5, difference)
        distance += difference ** 2
    metrics['distance'] = distance
    # Учитываем длину программы
    length = len(program)
    metrics['length'] = length
    return metrics

def fitness(program, expected, err_penalty=100000, dist_penalty=16, len_penalty=2, diff_penalty=1):
    m = get_metrics(program, expected)
    res = 0
    res += m['error'] * err_penalty
    res += m['distance'] * dist_penalty
    res += m['length'] * len_penalty
    res += m['diff'] * diff_penalty
    return res
