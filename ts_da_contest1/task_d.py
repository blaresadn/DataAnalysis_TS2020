n, k = input().split()
k = int(k)
k_sum = 0
for i in range(k):
    k_sum += int(n + n * i)
print(k_sum)
