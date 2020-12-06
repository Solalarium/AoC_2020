import sys
sys.path.insert(0, '.')
from util import Day
from day06 import *

def test_part1():
    day = Day(6,1)
    day.load(typing=str, sep='\n\n')
    day.answer(sum_groups(day.data))
    assert day.result == 6748

def test_part1_given_0():
    day = Day(6,1)
    day.load(typing=str, sep='\n\n', data='''abc

a
b
c

ab
ac

a
a
a
a

b'''.split('\n\n'))
    day.answer(sum_groups(day.data))
    assert day.result == 11

def test_part2():
    day = Day(6,2)
    day.load(typing=str, sep='\n\n')
    day.answer(sum_allyes(day.data))
    assert day.result == 3445

def test_part2_given_0():
    day = Day(6,2)
    day.load(typing=str, sep='\n\n', data='''abc

a
b
c

ab
ac

a
a
a
a

b'''.split('\n\n'))
    day.answer(sum_allyes(day.data))
    assert day.result == 6