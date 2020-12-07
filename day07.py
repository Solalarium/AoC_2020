from util import Day
import re

def prepare(data) -> dict:
    newdict = {}
    for i in data:
        i = i.split('s contain ')
        newdict[i[0]] = i[1]
    return(newdict)

def howmanycontain(data: dict, bag: str, counted: list):
    count = 0
    for i in data: #i is the bag
        if bag in data[i]:
            if not i in counted:
                count += 1
                count += howmanycontain(data, i, counted)
                counted.append(i)
    return(count)

def howmanyarecontained(data: dict, bag: str, counted: list):
    count = 0
    if bag in data:
        #data[bag] = 1 bright white bag, ...bag, 2 muted yellow bags.
        pass

    return(count)

if __name__ == '__main__':
    # --Part 1--
    part1 = Day(7,1)
    part1.load()

    part1.answer(howmanycontain(prepare(part1.data),'shiny gold bag',[]))
    print(part1.result)

    # --Part 2--
    part2 = Day(7,2)
    part2.load(data='''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''.split('\n'))

    part2.answer(prepare(part2.data))
    print(part2.result)