import sys
sys.path.insert(0, '.')
from util import Day
from day05 import *

def test_part1():
    day = Day(5,1)
    day.load(typing=str)
    day.answer(max_seatID(day.data))
    assert day.result == 892

def test_part1_given_0():
    day = Day(5,1)
    day.load(typing=str, data='FBFBBFFRLR'.split())
    day.answer(get_seatID(day.data[0]))
    assert day.result == 357

def test_part1_given_1():
    day = Day(5,1)
    day.load(typing=str, data='BFFFBBFRRR'.split())
    day.answer(get_seatID(day.data[0]))
    assert day.result == 567

def test_part1_given_2():
    day = Day(5,1)
    day.load(typing=str, data='FFFBBBFRRR'.split())
    day.answer(get_seatID(day.data[0]))
    assert day.result == 119

def test_part1_given_3():
    day = Day(5,1)
    day.load(typing=str, data='BBFFBBFRLL'.split())
    day.answer(get_seatID(day.data[0]))
    assert day.result == 820

def test_part2():
    day = Day(5,2)
    day.load(typing=str)
    day.answer(get_own_seatID())
    assert day.result == 625