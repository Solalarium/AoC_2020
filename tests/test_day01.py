import sys
sys.path.insert(0, '.')
from util import Day
from day01 import *


def test_part1():
    part1 = Day(1,1)
    part1.load(typing=int)
    part1.answer(find_2020(part1.data))
    assert part1.result == 482811

def test_part1_given_0():
    part1 = Day(1,1)
    part1.load(typing=int, data=[1721,979,366,299,675,1456])
    part1.answer(find_2020(part1.data))
    assert part1.result == 514579

def test_part2():
    part1 = Day(1,1)
    part1.load(typing=int)
    part1.answer(find_2020_with3(part1.data))
    assert part1.result == 193171814

def test_part2_given_0():
    part1 = Day(1,2)
    part1.load(typing=int, data=[1721,979,366,299,675,1456])
    part1.answer(find_2020_with3(part1.data))
    assert part1.result == 241861950