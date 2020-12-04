import sys
sys.path.insert(0, '.')
from util import Day
from day04 import *

def test_part1():
    day = Day(4,1)
    day.load(typing=str, sep='\n\n')
    day.answer(count_present(day.data))
    assert day.result == 213

def test_part1_given_0():
    day = Day(4,1)
    day.load(typing=str, sep='\n\n', data='''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''.split('\n\n'))
    day.answer(count_present(day.data))
    assert day.result == 2

def test_part2():
    day = Day(4,2)
    day.load(typing=str, sep='\n\n')
    day.answer(count_valid(day.data))
    assert day.result == 147
