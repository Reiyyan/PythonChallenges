def brangelina(first, second):
    vowel = ['a', 'e', 'i', 'o', 'u']
    previousFirst = False
    groupsFirst = 0
    vowelPositionsFirst = []
    
    # Check how many vowel groups in first
    for index, x in enumerate(first):

        # Mapping Position of Vowels and consonsnats for First Word
        if x in vowel:
            if(previousFirst == False):
                # print("New Vowel")
                groupsFirst += 1
                vowelPositionsFirst.append(index)
                previousFirst = True
                # We have a consoncant before so adding 
            else:
                # print("previousFirst Vowel")
                previousFirst = True
                # We had a previousFirst Vowel, so not adding anything
        else:
            # print('Consonant')
            previousFirst = False

    if(groupsFirst == 1):
        # print('In first Half')
        first = first[0:vowelPositionsFirst[0]]
    else:
        # print('In Second Half')
        first = first[0:vowelPositionsFirst[-2]]

    # print(firstCut)
    # print(vowelPositionsFirst[2])
 
    # print("printing Positions")
    # print(vowelPositionsFirst)

    for index, x in enumerate(second):
        if x in vowel:
            second = second[index:len(second)]
            break
        # else:
        #     second = second

    nickName = first + second

    return nickName


# print(brangelina("brad", 'angelina'))
# print(brangelina('angelina','brad'))

# print(brangelina('sheldon','amy'))
# print(brangelina('amy', 'sheldon'))
# print(brangelina('frank','ava'))
# print(brangelina('britain', 'exit'))
# print(brangelina('donald', 'hilary'))
# # print(brangelina())
