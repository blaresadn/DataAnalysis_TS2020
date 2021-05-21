n = int(input())
words = {}
for i in range(n):
    word = input()
    sort_word = ''.join(sorted(word))
    if sort_word in words:
        words[sort_word].append(word)
    else:
        words[sort_word] = [word]
for key in words:
    print(*words[key])
