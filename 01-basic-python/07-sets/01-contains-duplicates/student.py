def contains_duplicates(xs):
    if len(set(xs)) == len(xs):
        return False
    return True