import math

def fibonacci_word(k):
    golden = (1 + 5 ** 0.5) / 2
    digit = 2 + math.floor(k*golden) - math.floor((k+1)*golden)

    # return digit
    # cursor = 0
    # wordList = [0]

    # while cursor < k:
    #     if wordList[cursor] == 0:
    #         wordList.extend([1,0])
    #     if wordList[cursor] == 1:
    #         wordList.append(0)
    #     cursor +=1
    #     # del wordList[cursor]
    #     # k -= (len(wordList))

    return digit


# print(fibonacci_word(9))

def myRun(y):
    word = "0"
    i = 0
    while i < y:
        word = nextF(word)
        i+=1
        print(len(word))
    return word

def nextF(x):
    result =""
    word = x
    for c in word:
        if c == "0":
            result += "01"
        elif c == "1":
            result += "0"
    return result

# print(nextF("01001"))

# print(myRun(10))

print(fibonacci_word(100000000000))



# print('[a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, b, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, b, a, c, a, d, a, d, a, c, 0, b, 0, b, 0]')
# print('b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  b,  c,  d,  b,  b,  c,  d,  b,  b,  c,  d,  d,  b,  c,  d,  d,  b,  c,  d,  d,  c, 0, b, 0, b, 0')
# print('|  d,  |  d,  b,  |  b,  |  b,  |  d,  |  d,  b,  |  b,  |  b,  |  d,  |  d,  |  d,  b,  |  b,  |  d,  |  d,  |  d,  b,  |  b,  |  d,  |  d,  |  d,  b,  |  b,  |  b,  |  d,  |  d,  b,  |  b,  |  b,  |  d,  |  d,  |  d,  b,  |  b,  |  d,  |  d,  |  d,  b,  |  b,  |  d,  |  d,  |  d,  b,  |  b,  |  b,  |  d,  |  d,  b,  |  b,  |  b,  |  d,  |  d,  b,  |  b,  |  b,  |  d,  |  d,  |  d,  b,  |  b,  |  d,  |  d,  |  d,  b,  |  b,  |  b,  |  d,  |  d,  b,  |  b,  |  b,  |  d,  |  d,  b,  |  b,  |  b,  |  d,  |  d,  |  d,  b,  |  b,  |  d,  |  d,  |  d,  b,  |  b,  |  b,  |  d,  |  d,  b,  |  b,  |  b,  |  d,  |  d,  b,  |  b,  |  b,  |  d,  |  d,  |  d,  b,  |  b,  |  d,  |  d,  |  d,  b,  |  b,  |  d,  |  d,  |  d,  b,  |  b,  |  b,  |  d,  |  d,  b,  |  b,  |  b,  |  d,  |  d,  |  d,  b,  |  b,  |  d,  |  d,  |  d,  b,  |  b,  |  d,  |  d,  |  d,  b,  |  b,  |  b,  |  d,  |  d,  b,  |  b,  |  b,  |  d,  |  d,  b,  |  b,  |  b,  |  d,  |  d,  |  d,  b,  |  b,  |  d,  |  d,  |  d,  b,  |  b,  |  b,  |  d,  |  d,  b,  |  b,  |  b,  |  d,  |  d,  b,  |  b,  |  b,  |  d,  |  d,  |  d,  b,  |  b,  |  d,  |  d,  |  d,  b,  |  b,  |  b,  |  d,  |  d,  b,  |  b,  |  b,  |  d,  |  d,  b,  |  b,  |  b,  |  d,  |  d,  |  d,  b,  |  b,  |  d,  |  d,  |  d,  b,  |  b,  |  d,  |  d,  |  d,  b,  |  b,  |  b,  |  d,  |  d,  b,  |  b,  |  b,  |  d,  |  d,  |  ')

# 0, 1, 0, 0, 1, 0,
# 1, 0, 0, 1, 

# 0, 0, 1,