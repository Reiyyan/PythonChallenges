def riffle(items, out = True):
    firstList = items[:len(items)//2]
    secondList = items[len(items)//2:]
    result = []

    if(out):
        for i in range(len(items)//2):
            result.append(firstList[i])
            result.append(secondList[i])
    else:
        for i in range(len(items)//2):
            result.append(secondList[i])
            result.append(firstList[i])

    #print (result)
    return result


riffle([1, 2, 3, 4, 5, 6, 7, 8])
riffle([1, 2, 3, 4, 5, 6, 7, 8], False)
riffle([])
riffle(['bob', 'jack'])
riffle(['bob', 'jack'], False)
