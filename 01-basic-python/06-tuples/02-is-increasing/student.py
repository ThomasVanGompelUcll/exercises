def is_increasing(ns):
    ms = ns[1:]
    lst = list(zip(ns,ms))
    for pair in lst:
        if pair[0] > pair[1]:
            return False
    return True