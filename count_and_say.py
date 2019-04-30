def count_and_say(digits):
    myList = list(digits)
    # print(myList)
    myValue = None
    count = 0

    newString = ''

    for i in myList:
        if myValue == None:
            myValue = i
        if myValue == i:
            count+=1
        else:
            newString += str(count) + myValue
            myValue = i
            count = 1

    newString += str(count) + myValue

    return newString

# look at first number, get its value and add one to its count, go to next
# if same add to count, else add count and previous number to string, set new number add its counts

print(count_and_say('333388822211177'))