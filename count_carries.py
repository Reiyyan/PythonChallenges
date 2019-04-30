def count_carries(a, b):
    # listOfInt = list(str(a))
    # print(a//100%10)
    digitsA = len(str(abs(a)))
    digitsB = len(str(abs(b)))

    firstDict = {}
    secondDict = {}

    divider = 1

    for i in range(0,digitsA):
        digit = (a//divider)%10
        # print(digit)
        divider *= 10
        firstDict[i] = digit

    divider = 1
    for i in range(0,digitsB):
        digit = (b//divider)%10
        # print(digit)
        divider *= 10
        secondDict[i] = digit

    # print(firstDict)
    # print(secondDict)

    if digitsA > digitsB:
        bigger = digitsA
    else:
        bigger = digitsB

    carry = {}
    for i in range(bigger):
        x = firstDict.get(i,0) + secondDict.get(i,0) + carry.get(i,0)
        if x >= 10:
            carry[i+1] = x//10%10
        # print(x)

        # print(carry)
    return len(carry)

print(count_carries(3**1000,3**1000 + 1))