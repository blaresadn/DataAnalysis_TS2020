def brackets(n):
    f = True
    s = '(' * n + ')' * n
    yield s
    n *= 2
    while f:
        f = False
        depth = 0
        count = n - 1
        for c in s[::-1]:
            if c == '(':
                depth -= 1
            else:
                depth += 1
            if c == '(' and depth > 0:
                depth -= 1
                count1 = (n - count - 1 - depth) // 2
                count2 = n - count - 1 - count1
                s = s[:count] + ')' + count1 * '(' + count2 * ')'
                yield s
                f = True
                break
            count -= 1


if __name__ == '__main__':
    print(*list(brackets(int(input()))), sep='\n')
