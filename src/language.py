"""
Определение небольшого стекового языка аля-ассемблера
Память представляет собой стек неограниченной длины
Команды:
push - положить число 0 в стек
pop - вытолкнуть число из стека
neg - вытолкнуть число из стека, умножить его на -1 и положить результат в стек
xor - сложить два числа на вершине стека по модулю 2, и положить результат в стек
add - сложить два числа на вершине стека, и положить результат в стек
xorp - xor, но выталкиваем аргументы из стека
addp - add, но выталкиваем аргументы из стека
shlp - логический сдвиг влево числа на вершине стека
shrp - логический сдвиг вправо числа на вершине стека
inc - увеличить число на вершине стека на 1
dec - уменьшить число на вершине стека на 1
swap - обменять местами два числа на вершине стека
copy - скопировать число на вершине стека
Программа поступает в виде последовательности (списка) команд
Результат выполнения - состояние стека в конце выполнения программы
"""
import copy


class StackLang:
    def __init__(self):
        self._stack = []
        self.commands = {
            'push': self.push,
            'pop': self.pop,
            'xor': self.xor,
            'xorp': self.xorp,
            'add': self.add,
            'addp': self.addp,
            'neg': self.neg,
            'inc': self.inc,
            'dec': self.dec,
            'swap': self.swap,
            'copy': self.copy,
            'shlp': self.shlp,
            'shrp': self.shrp,
        }
        self.start = []

    def set_start(self, start):
        self.start = start

    def run(self, program):
        self._stack = copy.copy(self.start)
        try:
            for command in program:
                self.commands[command]()
        except Exception:
            return None
        return self.result()

    def run_generator(self, program):
        self._stack = copy.copy(self.start)
        try:
            for command in program:
                self.commands[command]()
                yield command, self.result()
        except Exception:
            return None
        return self.result()

    def push(self):
        self._stack.append(0)

    def pop(self):
        return self._stack.pop()

    def xor(self):
        self._stack.append(self._stack[-1] ^ self._stack[-2])

    def xorp(self):
        self._stack.append(self._stack.pop() ^ self._stack.pop())

    def add(self):
        self._stack.append(self._stack[-1] + self._stack[-2])

    def addp(self):
        self._stack.append(self._stack.pop() + self._stack.pop())

    def neg(self):
        self._stack.append(-self._stack.pop())

    def inc(self):
        self._stack[-1] += 1

    def dec(self):
        self._stack[-1] -= 1

    def swap(self):
        self._stack[-1], self._stack[-2] = self._stack[-2], self._stack[-1]

    def copy(self):
        self._stack.append(self._stack[-1])

    def shlp(self):
        self._stack[-1] <<= 1

    def shrp(self):
        self._stack[-1] >>= 1

    def reverse(self):
        self._stack.reverse()

    def result(self):
        return self._stack

runner = StackLang()