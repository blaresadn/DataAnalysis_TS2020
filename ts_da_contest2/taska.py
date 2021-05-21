def solution1(arg):
    return [x * 4 for x in arg]


def solution2(arg):
    return [arg[i - 1] * i for i in range(1, len(arg) + 1)]


def solution3(arg):
    return [x for x in arg if x % 3 == 0 or x % 5 == 0]


def solution4(arg):
    return [elem for sublist in arg for elem in sublist]


def solution5(arg):
    return [(a, b, c) for a in range(1, arg + 1) for b in range(a + 1, arg + 1) for c in range(b + 1, arg + 1)
            if a ** 2 + b ** 2 == c ** 2]


def solution6(arg):
    return [[x + i for x in arg[1]] for i in arg[0]]


def solution7(arg):
    return [[arg[i][j] for i in range(len(arg))] for j in range(len(arg[0]))]


def solution8(arg):
    return [[int(elem) for elem in sublist.split()] for sublist in arg]


def solution9(arg):
    return {k: v for k, v in zip([chr(ord('a') + i) for i in arg], [x ** 2 for x in arg])}


def solution10(arg):
    return {elem for elem in [name[0].upper() + name[1:] for name in
                              [name for name in [name.lower() for name in arg] if len(name) > 3]]}


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
