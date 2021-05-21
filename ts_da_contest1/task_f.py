sent1, sent2 = input().lower().split(), input().lower().split()
sent1_dict = {}
for word in sent1:
    if word in sent1_dict:
        sent1_dict[word] += 1
    else:
        sent1_dict[word] = 1
f = True
for word in sent2:
    if word in sent1_dict:
        if sent1_dict[word] < 1:
            f = False
            break
        sent1_dict[word] -= 1
    else:
        f = False
        break
if f:
    print('YES')
else:
    print('NO')
