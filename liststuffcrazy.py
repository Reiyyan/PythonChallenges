from operator import itemgetter

def highest_n_scores(scores, n = 5):
    myNameSet = set()
    index = 0
    resultList = []

    for name, point in scores:
        vars()[name] = list()
        myNameSet.add(name)

    individualList = [None for _ in range(len(myNameSet))]
    
    for name in myNameSet:
        individualList[index] = [name]
        for nameScore, point in scores:
            if nameScore == name:
                individualList[index].append(int(point))
        index +=1
    
    for reiList in individualList:  
        tempLeft = (reiList[0:1])
        tempRight = (reiList[1:])
        tempRight.sort(reverse=True)
        reiList = tempLeft + tempRight

        tempList = reiList[1:n+1]

        highScore = 0
        for i in tempList:
            highScore += int(i)

        resultList.append((reiList[0], highScore))  

    resultList.sort()

    return resultList




print(highest_n_scores([('bill', 10), ('jack', 6), ('sheldon', 3), ('tina', 2), ('amy', 3), ('sheldon', 6), ('tina', 7), ('jack', 2), ('bob', 3), ('bob', 4), ('bill', 3), ('bill', 9), ('sheldon', 5), ('amy', 2), ('jack', 7), ('sheldon', 5), ('sheldon', 7), ('bill', 1), ('bill', 9), ('sheldon', 5), ('bill', 2), ('bill', 6), ('jack', 6), ('bob', 4), ('tina', 5), ('sheldon', 4), ('sheldon', 2), ('amy', 6), ('bob', 7), ('jack', 2), ('bob', 5), ('sheldon', 9), ('jack', 5), ('amy', 9), ('bob', 7), ('tina', 6), ('tina', 2), ('amy', 7), ('jack', 10), ('tina', 4), ('bob', 5), ('jack', 10), ('bob', 7), ('jack', 5), ('amy', 4), ('amy', 8), ('bob', 4), ('bill', 8), ('bob', 6), ('tina', 6), ('amy', 9), ('bill', 4), ('jack', 2), ('amy', 2), ('amy', 4), ('sheldon', 1), ('tina', 3), ('bill', 9), ('tina', 4), ('tina', 9)], n=3))