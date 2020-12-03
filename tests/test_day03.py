import sys
sys.path.insert(0, '.')
from util import Day
from day03 import *

def test_part1():
    day = Day(3,1)
    day.load(typing=str)
    day.apply(list)
    day.answer(count_trees(day.data,3,1))
    assert day.result == 270

def test_part1_given_0():
    day = Day(3,1)
    day.load(typing=str, data='''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''.split())
    day.apply(list)
    day.answer(count_trees(day.data,3,1))
    assert day.result == 7

def test_part2():
    day = Day(3,2)
    day.load(typing=str)
    day.apply(list)
    day.answer(count_trees(day.data,1,1)*count_trees(day.data,3,1)*count_trees(day.data,5,1)*count_trees(day.data,7,1)*count_trees(day.data,1,2))
    assert day.result == 2122848000

def test_part2_given_0():
    day = Day(3,2)
    day.load(typing=str, data='''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''.split())
    day.apply(list)
    day.answer(count_trees(day.data,1,1)*count_trees(day.data,3,1)*count_trees(day.data,5,1)*count_trees(day.data,7,1)*count_trees(day.data,1,2))
    assert day.result == 336