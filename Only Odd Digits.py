def only_odd_digits(n):
    listOfInt = list(str(n))
    odd = True
    for i in listOfInt:
        if (int(i) % 2 != 0):
            odd = True
        elif (int(i) % 2 == 0):
            odd = False
            return odd
    return odd

print(only_odd_digits(1339))