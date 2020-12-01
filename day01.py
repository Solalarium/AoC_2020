from util import Day

def find_2020(data):
    for i in data:
        for j in data:
            if i + j == 2020:
                result = i * j
                break
    return(result)

def find_2020_with3(data):
    for i in data:
        for j in data:
            for k in data:
                if i + j + k == 2020:
                    result = i * j * k
                    break
    return(result)


if __name__ == '__main__':
    # --Part 1-- 482811
    part1 = Day(1,1)
    part1.load(int)

    print(part1.answer(find_2020(part1.data)))

    # --Part 2--
    part2 = Day(1,2)
    part2.load(int)

    print(part2.answer(find_2020_with3(part1.data)))
