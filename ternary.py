def balanced_ternary(n):

    return


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

        # print(myBalance[position])
        # print(type(myBalance[position]))

        if myBalance[position] == "2":
            # print("its 2")
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

            # myBalance.append("1")
            # if position == 0:
            #     myBalance.insert(0, '1')
            # elif position == (len(myBalance)-1):
            #     myBalance.append('1')
            # else:
            #     myBalance[position] = str(int(myBalance[position])+1)


            # myBalance[position+1] += "1"
    # print(myBalance)
    myBalance.reverse()
    return myBalance
    # myBalance = []

# print(balanced(2101))

print(balanced(22210))

# print(balanced("0102"))


# print(ternary(64))
print(ternary(237))
