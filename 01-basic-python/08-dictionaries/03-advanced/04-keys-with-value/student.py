# Write your code here
def keys_with_value(myDict, value):
    result = []
    for k in myDict.keys():
        if myDict[k] == value:
            result.append(k)
    return result