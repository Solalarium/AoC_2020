import sys
sys.path.insert(0, '.')
from util import Day
from day01 import *


def test_part1():
    day = Day(1,1)
    day.load(typing=int)
    day.answer(find_2020(day.data))
    assert day.result == 482811

def test_part1_given_0():
    day = Day(1,1)
    day.load(typing=int, data=[1721,979,366,299,675,1456])
    day.answer(find_2020(day.data))
    assert day.result == 514579

def test_part2():
    day = Day(1,1)
    day.load(typing=int)
    day.answer(find_2020_with3(day.data))
    assert day.result == 193171814

def test_part2_given_0():
    day = Day(1,2)
    day.load(typing=int, data=[1721,979,366,299,675,1456])
    day.answer(find_2020_with3(day.data))
    assert day.result == 241861950