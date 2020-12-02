import sys
sys.path.insert(0, '.')
from util import Day
from day02 import *

def test_part1():
    day = Day(2,1)
    day.load(typing=str)
    day.answer(count_valid_passwords(day.data))
    assert day.result == 418

def test_part1_given_0():
    day = Day(2,1)
    day.load(typing=str, data=['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc'])
    day.answer(count_valid_passwords(day.data))
    assert day.result == 2

def test_part2():
    day = Day(2,1)
    day.load(typing=str)
    day.answer(count_valid_passwords_new(day.data))
    assert day.result == 616

def test_part2_given_0():
    day = Day(2,1)
    day.load(typing=str, data=['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc'])
    day.answer(count_valid_passwords_new(day.data))
    assert day.result == 1