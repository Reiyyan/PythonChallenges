import random

def first_missing_positive(items):
    x = set(items)
    # print(x)
    for i in range(1,max(x)+1):
        if i not in x:
            return i
    return max(x)+1




# print(first_missing_positive([7, 5, 2, 3, 10, 2, 99999, 4, 6, 3, 1, 9, 2]))
print(first_missing_positive(list(range(100000, 2, -1))))

y = (list(range(1000000)))
random.shuffle(y)

print(first_missing_positive(y))
    # [7, 5, 2, 3, 10, 2, 99999999999, 4, 6, 3, 1, 9, 2]