from util import Day
from string import ascii_lowercase

def get_group_answers(data):
    data = data.split('\n')
    answers = {}
    for i in data:
        # i represents single persons answer as a single string
        for j in i:
            answers[j] = 1
    return(len(answers))

def get_allyes_answers(data):
    data = data.split('\n')
    answers = {}
    for i in ascii_lowercase:
        answers[i] = True
    count = 0
    for i in data:
        # i represents single persons answer as a single string
        for j in answers:
            if not j in i:
                answers[j] = False
    for i in answers:
        if answers[i]: count += 1
    return(count)

def sum_groups(data):
    count = 0
    for i in data:
        count += get_group_answers(i)
    return(count)

def sum_allyes(data):
    count = 0
    for i in data:
        count += get_allyes_answers(i)
    return(count)

if __name__ == '__main__':
    # --Part 1-- 6748
    part1 = Day(6,1)
    part1.load(sep='\n\n')

    part1.answer(sum_groups(part1.data))
    print(part1.result)

    # --Part 2-- 3445
    part1 = Day(6,2)
    part1.load(sep='\n\n')

    part1.answer(sum_allyes(part1.data))
    print(part1.result)