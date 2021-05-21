change = float(input())
coins = [10, 5, 2, 1, 0.5, 0.1, 0.05, 0.01]
ch_dict = {}
for coin in coins:
    ch_dict[coin] = change // coin
    change -= coin * ch_dict[coin]
if change > 0.001:
    ch_dict[0.01] = ch_dict.get(0.01, 0) + 1
for elem in ch_dict:
    if ch_dict[elem]:
        print('%5.2f\t%d' % (elem, ch_dict[elem]))
