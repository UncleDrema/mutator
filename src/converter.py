"""
Преобразоавние программ из строки и в строку
"""

def to_str(program):
    """
    Преобразование программы в строку
    """
    # Преобразуем каждую команду в строку
    # и объединяем их через перенос строки
    return '\n'.join(program)

def from_str(program):
    """
    Преобразование программы из строки
    """
    # Оставляем только непустые строки,
    # обрезаем лишние пробелы по краям
    # оставляем первое слово как команду, остальное - как аргументы (и приводим к int)
    lines = [line.strip().split() for line in program.split('\n') if line.strip()]
    return [[line[0], *map(int, line[1:])] for line in lines]