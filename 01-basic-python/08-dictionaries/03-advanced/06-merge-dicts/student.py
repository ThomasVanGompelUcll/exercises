# Write your code here
def merge_dicts(myDict1, myDict2):
    result = myDict1.copy()
    for k, v in myDict2.items():
        result[k] = v
    return result 