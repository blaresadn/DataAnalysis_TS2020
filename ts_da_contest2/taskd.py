import functools


def counter(func):
    setattr(counter, 'rdepth', 0)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, 'ncalls'):
            setattr(wrapper, 'ncalls', 0)
        if not hasattr(wrapper, 'rdepth'):
            setattr(wrapper, 'rdepth', 0)
        if counter.rdepth == 0:
            wrapper.ncalls = 0
            wrapper.rdepth = 0
        counter.rdepth += 1
        wrapper.ncalls += 1
        wrapper.rdepth = max(wrapper.rdepth, counter.rdepth)
        res = func(*args, **kwargs)
        counter.rdepth -= 1
        return res
    return wrapper
