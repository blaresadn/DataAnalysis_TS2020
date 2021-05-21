n = input()
inp_list = input().split()
new_list = []
for elem in inp_list:
    if elem not in new_list:
        new_list.append(elem)
print(*new_list)
print(len(inp_list) - len(new_list))
