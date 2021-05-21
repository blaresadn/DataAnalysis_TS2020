def divide(b1, b2):
    parts = (min(8, b2 - b1))
    part = (b2 - b1) / parts
    mids_list = [b1]
    for j in range(1, parts):
        mids_list.append(int(b1 + part * j))
    mids_list.append(b2)
    return mids_list


mids = divide(0, 100001)
ans = -1
while True:
    len_mids = len(mids)
    for elem in mids[1:len_mids - 1]:
        print('?', elem, flush=True)
    print('+', flush=True)
    answers = []
    for i in range(len_mids - 2):
        answers.append(int(input()))
    f = False
    for i in range(1, len_mids):
        if i == len_mids - 1 or answers[i - 1]:
            if len_mids < 9:
                ans = mids[answers.count(0)]
                f = True
            mids = divide(mids[i - 1], mids[i])
            break
    if f:
        break
print('!', ans, flush=True)
