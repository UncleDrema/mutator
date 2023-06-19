from src.fitness import fitness, get_metrics
from src.language import runner
from src.mutator import mutator


def remove_duplicates(new_programs):
    # На входе - список списков строк
    # На выходе - список списков строк без дубликатов
    # Пример: [['push'], ['push'], ['pop']] -> [['push'], ['pop']]
    res = []
    for prog in new_programs:
        if prog not in res:
            res.append(prog)
    return res


def run_genetic(start, target, take=10, max_iter=1000, iter_step=100, execute=False, verbose=False):
    runner.set_start(start)
    programs = [[]]
    best_score = int(1e9)
    best_program = []
    for i in range(max_iter):
        new_programs = []
        # Получаем варианты программ
        if len(programs) > 0:
            for prog in programs:
                new_programs.extend(mutator.get_mutated(prog))

        # Выводим лучший результат
        if verbose and i % iter_step == 0:
            print(f'Iteration {i}, best score: {best_score}')

        # Считаем фитнес-функцию для каждой программы и сохраняем пары (программа, оценка)
        program_scores = []
        for prog in new_programs:
            fit = fitness(prog, target)
            program_scores.append((prog, fit))

        # Сортируем по фитнесу
        program_scores.sort(key=lambda x: x[1])
        # Оставляем только лучшие
        program_scores = program_scores[:take]
        # Сохраняем лучший результат
        if len(program_scores) > 0 and program_scores[0][1] < best_score:
            best_score = program_scores[0][1]
            best_program = program_scores[0][0]

        # Оставляем только программы
        new_programs = [x[0] for x in program_scores]

        # Удаляем дубликаты
        new_programs = remove_duplicates(new_programs)

        # Если не осталось, начинаем с мутаций лучшей программы
        if len(new_programs) == 0:
            new_programs = mutator.get_mutated(best_program)
        programs = new_programs

    print(f'Best program: {best_program}\nBest result: {runner.run(best_program)}\nWhen expected: {target}')
    metrics = get_metrics(best_program, target)
    print(f'Error: {metrics["error"]}\nDistance: {metrics["distance"]}\nLength: {metrics["length"]}\nDiff: {metrics["diff"]}\nTotal score: {best_score}')
    if execute:
        print('Executing best program:')
        print(f'Start stack: {start}')
        for command, stack in runner.run_generator(best_program):
            print(f'{command}: {stack}')
