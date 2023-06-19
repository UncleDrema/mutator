import pytest

from src.converter import to_str, from_str


# тест на преобразование из строки с параметрами
@pytest.mark.parametrize('program, expected', [
    ('', []),
    ('push', [['push']]),
    ('push\npush\npop', [['push'], ['push'], ['pop']]),
    ('push    \n\npush\n add  ', [['push'], ['push'], ['add']]),
])
def test_from_str(program, expected):
    assert from_str(program) == expected


# тест на преобразование в строку с параметрами
@pytest.mark.parametrize('program, expected', [
    ([], ''),
    ([['push']], 'push'),
    ([['push'], ['push'], ['swap', 1]], 'push\npush\nswap 1'),
])
def test_to_str(program, expected):
    assert to_str(program) == expected
