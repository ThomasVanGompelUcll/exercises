def contains_duplicates(xs):
    for i in xs:
        count = 0
        for j in xs:
            if i == j:
                count += 1
        if count >= 2:
            return True
    return False 


