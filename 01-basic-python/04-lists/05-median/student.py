def median(list):
    list = sorted(list)
    print(len(list)//2)
    if len(list) % 2 == 0:
        return (list[len(list)//2]+list[len(list)+1]) / 2
    else:
        return list[len(list)+1]


