def create_zigzag(rows, cols, start = 1):
    mainList = []
    i = 1
    # point = start
    while (i <= rows):
        # myList = list(range(i*cols-cols+1, i*cols+1, start))
        if(i == 1):
            myList = list(range(start*i, (start*i)+cols))
        else:
            myList = list(range(start+(i-1)*cols, start+(i)*cols))
        # print(myList)
        if ((i-1) % 2 == 0):
            mainList.append(myList)
        else:
            myList.reverse()
            mainList.append(myList)
        i+=1
    return mainList

print(create_zigzag(3,5))

# print(create_zigzag(10,1))
# print(create_zigzag(4,2))


# for x in range(10):
#     print (x)

# newList = list(range(1,11))
# print(newList)