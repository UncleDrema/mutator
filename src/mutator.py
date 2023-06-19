"""
Мутатор для изменения программы на StackLang
Мутатор может удалять команды, добавлять новые в произвольное место программы и заменять одни команды на другие
А также может менять порядок двух команд в программе и менять числовые аргументы команд на +1 или -1
"""

import random
import copy
import itertools
from src.language import runner

"""
Мутатор возвращает результат каждого возможного изменения при вызове на программе
"""


class Mutator:
    def __init__(self):
        self.mutators = [self.mutate_delete, self.mutate_add, self.mutate_replace, self.mutate_swap]

    @staticmethod
    def gen_random_command():
        commands = list(runner.commands.keys())
        command = random.choice(commands)
        return command

    # Удаляем команду по случайной позиции
    @staticmethod
    def mutate_delete(program: list):
        n = len(program)
        if n > 0:
            program.pop(random.randrange(0, n))

    # Добавляем случайную команду на позиции
    @staticmethod
    def mutate_add(program: list):
        n = len(program)
        command = Mutator.gen_random_command()
        if n > 0:
            program.insert(random.randrange(0, n), command)
        else:
            program.append(command)

    # Заменяем случайную команду на случайную
    @staticmethod
    def mutate_replace(program: list):
        n = len(program)
        if n > 0:
            program[random.randrange(0, n)] = Mutator.gen_random_command()

    # Меняем порядок двух случайных команд
    @staticmethod
    def mutate_swap(program: list):
        n = len(program)
        if n > 1:
            i, j = random.sample(range(n), 2)
            program[i], program[j] = program[j], program[i]

    def get_mutated(self, program):
        res = [program]
        for mutator in self.mutators:
            new_program = copy.deepcopy(program)
            mutator(new_program)
            res.append(new_program)
        return res

    @staticmethod
    def generate_one_command_programs(count=1):
        res = []
        for i in range(count):
            res.append([Mutator.gen_random_command()])
        return res


mutator = Mutator()
