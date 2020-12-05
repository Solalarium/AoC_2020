from util import Day

seatIDs = []
#128rows 0-127
#8columns 0-7
def get_seatID(data):
    row_start = 0
    row_end = 127
    col_start = 0
    col_end = 7
    for i in data:
        if i == 'F':
            row_end = row_end-(((row_end-row_start)//2)+1)
        elif i == 'B':
            row_start = row_start+(((row_end-row_start)//2)+1)
        elif i == 'L':
            col_end = col_end-(((col_end-col_start)//2)+1)
        elif i == 'R':
            col_start = col_start+(((col_end-col_start)//2)+1)
    return(row_end*8+col_end)

def max_seatID(data):
    maximum = 0
    for i in data:
        x = get_seatID(i)
        seatIDs.append(x)
        if x > maximum: maximum = x
    return(maximum)

def get_own_seatID():
    seatIDs.sort()
    for i in range(len(seatIDs)-1):
        if i != 0:
            if not seatIDs[i-1]+1 == seatIDs[i] == seatIDs[i+1]-1:
                return(seatIDs[i]+1)
    return(0)

if __name__ == '__main__':
    # --Part 1-- 892
    part1 = Day(5,1)
    part1.load()

    part1.answer(max_seatID(part1.data))
    print(part1.result)

    # --Part 2-- 625
    part2 = Day(5,2)
    part2.load()

    part2.answer(get_own_seatID())
    print(part2.result)