def chain_loop(args):
    args = list(map(iter, args))
    k = 0
    i = -1
    cur_args = args
    while k < len(args):
        i = (i + 1) % len(cur_args)
        try:
            yield next(cur_args[i])
        except StopIteration as e:
            cur_args = cur_args[:i] + cur_args[i + 1:]
            k += 1
