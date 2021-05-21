numbers = list(map(int, input().split()))
cur = numbers[0]
beg, end, step = cur, cur + 1, 1
for elem in numbers[1:]:
    if beg == cur:
        step = elem - cur
        if not step:
            step = 1
    if elem - cur != step:
        if step > 0:
            end = cur + 1
        else:
            end = cur - 1
        print(beg, end, step)
        beg = elem
        step = 1
    cur = elem
if step > 0:
    end = cur + 1
else:
    end = cur - 1
print(beg, end, step)
