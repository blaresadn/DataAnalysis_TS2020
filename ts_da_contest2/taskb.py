import re
from functools import reduce


def solution1(arg):
    return list(map(lambda y: int(''.join(y)), map(lambda x: reversed(re.findall('[0-9]', x)), arg)))


def solution2(arg):
    return list(map(lambda x: x[0] * x[1], list(arg)))


def solution3(arg):
    return list(filter(lambda x: x % 6 == 0 or x % 6 == 2 or x % 6 == 5, arg))


def solution4(arg):
    return list(filter(lambda x: bool(x), arg))


def solution5(arg):
    return list(map(lambda d: d.__setitem__('square', d['width'] * d['length']) or d, arg))


def solution6(arg):
    return list(map(lambda d: dict(d, square=d['width'] * d['length']), arg))


def solution7(arg):
    return reduce(lambda x, y: x & y, arg)


def solution8(arg):
    return reduce(lambda d, x: d.__setitem__(x, arg.count(x)) or d, arg, {})


def solution9(arg):
    return reduce(lambda l, d: l.append(d['name']) or l if d['gpa'] > 4.5 else l, arg, [])


def solution10(arg):
    return list(filter(lambda x: sum(map(int, list((x[::2])))) == sum(map(int, list(x[1::2]))), arg))


solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
}
