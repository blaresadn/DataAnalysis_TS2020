def digit_sum(x):
    x_sum = 0
    while x:
        x_sum += x % 10
        x //= 10
    return x_sum


n = input()
inp_list = list(map(int, input().split()))
inp_list.sort(key=lambda x: (digit_sum(x), x))
print(*inp_list)
