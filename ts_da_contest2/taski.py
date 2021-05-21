from copy import copy, deepcopy


class FragileDict:
    def __init__(self, inp_dict=None):
        self._lock = True
        if inp_dict is None:
            self._data = {}
        else:
            self._data = deepcopy(inp_dict)

    def __enter__(self):
        self._lock = False
        self._data_copy = deepcopy(self._data)
        return self

    def __getitem__(self, key):
        if key not in self._data:
            raise KeyError(key)
        if self._lock:
            return copy(self._data[key])
        return self._data[key]

    def __setitem__(self, key, val):
        if self._lock:
            raise RuntimeError("Protected state")
        self._data[key] = val

    def __contains__(self, elem):
        return elem in self._data

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self._lock = True
        if exc_type is None:
            self._data = deepcopy(self._data)
        else:
            self._data = self._data_copy
            del self._data_copy
            print('Exception has been suppressed.')
            return True
