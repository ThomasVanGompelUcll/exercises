# Write your code here
def create_dictionary(keys, values):
    if(len(keys) == 0):
        return {}
    myDict = dict()
    for i in range(len(keys)):
        myDict[keys[i]] = values[i]
    return myDict

create_dictionary([1,2,3,4],["a","b","c","d"])