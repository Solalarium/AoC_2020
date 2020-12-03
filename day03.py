from util import Day

def count_trees(data,r,d):
    x = 0
    y = 0
    count = 0
    while y in range(len(data)):
        if x >= len(data[y]):
            data = extend(data)
        if data[y][x] == '#':
            count += 1
        x += r
        y += d

    return(count)

def extend(data):
    for i in range(len(data)):
        data[i].extend(data[i])
    return(data)

if __name__ == '__main__':
    # --Part 1-- 270
    part1 = Day(3,1)
    part1.load()
    part1.apply(list)

    print(part1.answer(count_trees(part1.data,3,1)))

    # --Part 2-- 2122848000
    part2 = Day(3,2)
    part2.load()
    part2.apply(list)

    part2.answer(count_trees(part2.data,1,1)*count_trees(part2.data,3,1)*count_trees(part2.data,5,1)*count_trees(part2.data,7,1)*count_trees(part2.data,1,2))

    print(part2.answer())