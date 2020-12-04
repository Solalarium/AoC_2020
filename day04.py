from util import Day
import re

def prepare(data):
    new_data = []
    for i in data:
        x = i.replace('\n',' ').split(' ')
        y = []
        for j in x:
            y.append(tuple(j.split(':')))
        new_data.append(dict(y))
    return(new_data)

def is_present(data):
    if 'byr' in data and 'iyr' in data and 'eyr' in data and 'hgt' in data and 'hcl' in data and 'ecl' in data and 'pid' in data:
        return(True)
    else: return(False)
def is_valid(data):
    # byr
    if not 1920 <= int(data['byr']) <= 2002: return(False)
    # iyr
    if not 2010 <= int(data['iyr']) <= 2020: return(False)
    # eyr
    if not 2020 <= int(data['eyr']) <= 2030: return(False)
    # hgt
    if not check_hgt(data['hgt']): return(False)
    # hcl
    if not check_hcl(data['hcl']): return(False)
    # ecl
    if not check_ecl(data['ecl']): return(False)
    # pid
    if not check_pid(data['pid']): return(False)
    return(True)

def check_hgt(hgt):
    if hgt.endswith('cm'):
        if 150 <= int(hgt.rstrip('cm')) <= 193: return(True)
    elif hgt.endswith('in'):
        if 59 <= int(hgt.rstrip('in')) <= 76: return(True)
    else: return(False)

def check_hcl(hcl):
    return re.search('^#([0-9a-f]){6}$',hcl)

def check_ecl(ecl):
    return re.search('^(amb|blu|brn|gry|grn|hzl|oth){1}$',ecl)

def check_pid(pid):
    return re.search('^[0-9]{9}$',pid)
    
def count_present(data):
    count = 0
    data = prepare(data)
    for i in data: 
        if is_present(i): count += 1
    return(count)

def count_valid(data):
    count = 0
    data = prepare(data)
    for i in data:
        if is_present(i):
            if is_valid(i): count += 1
    return(count)

if __name__ == '__main__':
    # --Part 1-- 213
    part1 = Day(4,1)
    part1.load(sep="\n\n")

    part1.answer(count_present(part1.data))
    print(part1.result)

    # --Part 2--
    part1 = Day(4,2)
    part1.load(sep="\n\n")

    part1.answer(count_valid(part1.data))
    print(part1.result)