import src.converter as converter
from src.language import runner
from src.mutator import mutator
from src.fitness import fitness


def remove_duplicates(new_programs):
    # На входе - список списков строк
    # На выходе - список списков строк без дубликатов
    # Пример: [['push'], ['push'], ['pop']] -> [['push'], ['pop']]
    res = []
    for prog in new_programs:
        if prog not in res:
            res.append(prog)
    return res


def main():
    start = [-21]
    runner.set_start(start)
    target = [21]
    take = 20
    programs = [['push']]
    best_fitness = int(1e9)
    best_program = []
    max_iter = 1000
    for i in range(max_iter):
        new_programs = []
        # Получаем варианты программ
        if len(programs) > 0:
            for prog in programs:
                new_programs.extend(mutator.get_mutated(prog))
        print(f'Iteration {i}, best fitness: {best_fitness}')

        # Считаем фитнес-функцию для каждой программы и сохраняем пары (программа, фитнес)
        fitnesses = []
        for prog in new_programs:
            fit = fitness(prog, target)
            fitnesses.append((prog, fit))

        # Сортируем по фитнесу
        fitnesses.sort(key=lambda x: x[1])
        # Оставляем только лучшие
        fitnesses = fitnesses[:take]
        # Сохраняем лучший результат
        if len(fitnesses) > 0 and fitnesses[0][1] < best_fitness:
            best_fitness = fitnesses[0][1]
            best_program = fitnesses[0][0]

        new_programs = [x[0] for x in fitnesses]

        new_programs = remove_duplicates(new_programs)

        # Если не осталось, начинаем с нуля
        if len(new_programs) == 0:
            new_programs = mutator.get_mutated(best_program)
        programs = new_programs

    print(f'Best fitness: {best_fitness}, best program: {best_program}')
    print(f'Best result: {runner.run(best_program)}, expected: {target}')
    print(f'My: {runner.run(["add", "swap", "pop", "swap", "pop"])}')


if __name__ == '__main__':
    main()