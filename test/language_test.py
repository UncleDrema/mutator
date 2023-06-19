import pytest
from src.language import runner


def program_test(program, expected):
    assert runner.run(program) == expected


def test_empty():
    program_test([], [])


def test_push():
    program_test(['push'], [0])



def test_pop():
    program_test(['push', 'pop'], [])


def test_xor():
    program_test(['push', 'inc', 'push', 'inc', 'xor'], [1, 1, 0])


def test_inc():
    program_test(['push', 'inc'], [1])

def test_dec():
    program_test(['push', 'dec'], [-1])

def test_swap():
    program_test(['push', 'inc', 'push', 'swap'], [0, 1])

def test_copy():
    program_test(['push', 'copy'], [0, 0])

