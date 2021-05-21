from collections import defaultdict


def smartdict_nan(key):
    return lambda: 10 * key


N = 10
smartdict = {}
for key in range(N):
    val = defaultdict(smartdict_nan(key))
    smartdict[key] = val

"""
В первом случае программа работала не так, как мы ожидали, потому что мы сразу передевали в конструктор defaultdict
callable-объект (lambda: smartdict_nan(key)), и это работло так, что если в defaultdict не находился ключ 'key_unknown',
то его значением становился результат выполнения smartdict_nan(key). К тому времени, когда мы пытались извлечь из
defaultdict ключ, которого еще нет в словаре, key уже был равен 9 (к концу цикла), поэтому мы получали результат
выполнения smartdict_nan(9). Во втором случае конструктор defaultdict получал callable-объект не сразу, а после
выполнения smartdict_nan(key), то есть, функция выполнялась сразу и принимала соотвестсвующие значения (0-9), а сам
конструктор уже принимал lambda-функцию lambda: 10 * key_i, где i - порядок вызова smartdict_nan.
"""
