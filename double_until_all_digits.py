def double_until_all_digits(n, giveup = 1000):
    index = 0
    # print(list(str(n)))
    while(index <= giveup):
        # print(f"Test #{index}")
        if(doubleTest(n)):
            return index
        else:
            n*=2
            index += 1
    return -1

def doubleTest(n):
    for i in range(10):
        if str(i) not in list(str(n)):
            # print(f'comparing {i} to {list(str(n))}')
            # print(i)
            return False
    return True

print(double_until_all_digits(1))
# 1
# 1000
