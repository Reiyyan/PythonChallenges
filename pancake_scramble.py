def pancake_scramble(text):
    x = len(text)
    i = 2
    myText = text
    while(i <= x):
        myText = pancake_flip(myText, i)
        i+=1
    return myText

def pancake_flip(text, number):
    # slice number from text
    a = text[0:number]
    b = text[number:]
    # print(a)
    # print(b)

    # flip letters
    a = a[::-1]

    # concat strings
    c = a+b
    return c

# print(pancake_flip("test",2))
print(pancake_scramble("abcdef"))