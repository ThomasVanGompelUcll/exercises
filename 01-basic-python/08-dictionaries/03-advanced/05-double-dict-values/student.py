# Write your code here
def double_dict_values(myDict):
    result = dict()
    for k, v in myDict.items():
        result[k] = v*2
    return result