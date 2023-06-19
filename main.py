from src.genetic_runner import run_genetic
from sys import argv
import argparse


if __name__ == '__main__':
    # Первый аргумент - список начального значения стека в формате 1,2,3
    # Второй аргумент - список ожидаемого результата в формате 1,2,3
    # Третий аргумент - число поколений (--iter=1000)
    # Четвертый аргумент - число особей, выбираемых на каждом поколении (--take=10)
    # Пятый аргумент - число итераций, через которое выводится лучший результат (--step=100)
    # Также параметр -e (--exec) для запуска программы с лучшим результатом с выводом стека на каждом шаге
    parser = argparse.ArgumentParser(description='Genetic algorithm for stack machine')
    parser.add_argument('target', metavar='target', type=str, help='Target stack: 1,2,3')
    parser.add_argument('--start', metavar='start', type=str, default='0', help='Start stack: 1,2,3')
    parser.add_argument('--iter', metavar='iter', type=int, default=1000, help='Number of iterations')
    parser.add_argument('--take', metavar='take', type=int, default=10, help='Number of programs to take')
    parser.add_argument('--step', metavar='step', type=int, default=100, help='Number of iterations between output')
    parser.add_argument('-e', '--exec', action='store_true', help='Execute best program')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    args = parser.parse_args()
    try:
        start = [int(x) for x in args.start.split(',')]
        target = [int(x) for x in args.target.split(',')]
    except ValueError:
        print('Invalid input: start and target should be comma-separated lists of integers')
        exit(1)
    print('Running genetic algorithm with parameters:')
    print(f'Start stack: {start}')
    print(f'Target stack: {target}')
    print(f'Number of iterations: {args.iter}')
    print(f'Number of programs to take: {args.take}')
    print(f'Number of iterations between output: {args.step}')
    run_genetic(start, target, args.take, args.iter, args.step, args.exec, args.verbose)
