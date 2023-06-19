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


def fitness(program, expected, err_penalty=10000, dist_penalty=64, len_penalty=8, diff_penalty=1):
    expected = copy.copy(expected)
    result = runner.run(program)
    if result is None:
        return err_penalty
    res = 0
    # Считаем "Расстояние" между полученным и ожидаемым результатом
    diff = abs(len(result) - len(expected))
    res += diff * diff_penalty
    # Сначала дополним их нулями до одинаковой длины
    fill_results(result, expected)
    # Теперь считаем расстояние
    distance = 0
    for i in range(len(result)):
        distance += abs(result[i] - expected[i])
    res += distance * dist_penalty
    # Учитываем длину программы
    length = len(program)
    res += length * len_penalty
    return res