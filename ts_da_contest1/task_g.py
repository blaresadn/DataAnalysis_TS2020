numbers = list(map(int, input().split()))
if len(numbers) == 2:
    if numbers[0] > numbers[1]:
        print(numbers[1], numbers[0])
    else:
        print(numbers[0], numbers[1])
else:
    max_pos1 = 0
    max_pos2 = 0
    max_neg1 = 0
    max_neg2 = 0
    for elem in numbers:
        if elem > max_pos1:
            max_pos2 = max_pos1
            max_pos1 = elem
        elif elem > max_pos2:
            max_pos2 = elem
        if elem < max_neg1:
            max_neg2 = max_neg1
            max_neg1 = elem
        elif elem < max_neg2:
            max_neg2 = elem
    if max_pos1 * max_pos2 >= max_neg1 * max_neg2:
        print(max_pos2, max_pos1)
    else:
        print(max_neg1, max_neg2)
