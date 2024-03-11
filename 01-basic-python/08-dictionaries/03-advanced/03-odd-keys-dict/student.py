# Write your code here
def odd_keys_dict(myDict):
    result = dict()
    for key in myDict:
        print(key)
        if key % 2 != 0:
            result[key] = myDict[key]
    return result
    

odd_keys_dict({1: 'a', 2: 'b', 3: 'c'})