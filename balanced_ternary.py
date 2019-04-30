def balanced_ternary(n):
    negative = False
    
    if(n < 0):
        n *= -1
        negative = True

    x = ternary(n)
    x = balanced(x)

    i=0
    answer = []
    # print(x)
    x.reverse()

    for b in x:
        if b == "Z":
            multiplier = -1
        elif b == "0":
            multiplier = 0
        else:            
            multiplier = 1

        decimal = (3**i * multiplier)
        if decimal != 0:
            answer.append(decimal)
        i+=1

    # print(x)

    answer.reverse()

    if negative:
        for i in range(len(answer)):
            answer[i] *= -1

    return answer

def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

def balanced(n):
    myBalance = list(str(n))
    if n == 0:
        return '0'

    myBalance.reverse()

    for position in range(len(myBalance)):

        if myBalance[position] == "2":
            myBalance[position] = 'Z'
            if position < len(myBalance)-1:
                myBalance[position + 1] = str(int(myBalance[position + 1]) + 1)
            else:
                myBalance.append('1')

        if myBalance[position] == "3":
            myBalance[position] = '0'
            if position < len(myBalance)-1:
                myBalance[position + 1] = str(int(myBalance[position + 1]) + 1)
            else:
                myBalance.append('1')

    myBalance.reverse()

    return myBalance

# print(balanced(2101))

# print(balanced(22210))

# print(balanced("0102"))


# print(ternary(64))
# print(ternary(237))
# print(balanced_ternary(10**6))
print(balanced_ternary(-5))
# print(ternary(-5))
