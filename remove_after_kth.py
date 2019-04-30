def remove_after_kth(items, k = 1):
    myDict = {}
    myList = []
    for i in items:
        myDict[i] = myDict.get(i, 0) + 1
        if myDict[i] <= k:
            myList.append(i)
    return myList

print(remove_after_kth([42, 42, 42, 42, 42, 42, 42],0))