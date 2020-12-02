from util import Day

def count_valid_passwords(data):
    count = 0
    for i in data:
        x = i.split(':')
        x[0] = x[0].split(' ')
        x.insert(0, x[0].pop(0))
        x[1] = x[1][0]
        low = int(x[0].split('-')[0])
        high = int(x[0].split('-')[1])
        if low <= x[2].count(x[1]) <= high:
            count += 1
    return (count)

def count_valid_passwords_new(data):
    count = 0
    for i in data:
        x = i.split(':')
        x[0] = x[0].split(' ')
        x.insert(0, x[0].pop(0))
        x[1] = x[1][0]
        x[2] = x[2].strip()
        low = int(x[0].split('-')[0])
        high = int(x[0].split('-')[1])
        if (x[2][low-1] == x[1] and x[2][high-1] != x[1]) or (x[2][low-1] != x[1] and x[2][high-1] == x[1]):
            count += 1
    return (count)


if __name__ == '__main__':
    # --Part 1-- 418
    part1 = Day(2,1)
    part1.load(str)

    print(part1.answer(count_valid_passwords(part1.data)))

    # --Part 2-- 616
    part1 = Day(2,2)
    part1.load(str)

    print(part1.answer(count_valid_passwords_new(part1.data)))