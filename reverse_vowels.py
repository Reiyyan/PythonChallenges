from collections import deque

def reverse_vowels(text):
    listText = list(text)

    vowels =  {'a','e','i','o','u','A','E','I','O','U'}

    indexList = deque()

    # print(text[::-1])

    
    for i in range(len(listText)):
        if listText[i] in vowels:
            indexList.append(i)
            # print(i)
    
    for _ in range(len(indexList)):
        if len(indexList) <= 1:
            print(len(indexList))
            break
        left = indexList.popleft()
        # print(left)
        right = indexList.pop()
        # print(right)
        if listText[left].isupper() and listText[right].islower():
            listText[left], listText[right] = listText[right].upper(), listText[left].lower()
        elif listText[left].islower() and listText[right].isupper():
            listText[left], listText[right] = listText[right].lower(), listText[left].upper()
        else:
            listText[left], listText[right] = listText[right], listText[left]


    result = "".join(listText)
    # print(indexList)

    # print(listText)

    return result


print(reverse_vowels('Hello world'))

print(reverse_vowels('Ilkka Markus Kokkarinen'))

print(reverse_vowels('This is Computer Science I!'))
