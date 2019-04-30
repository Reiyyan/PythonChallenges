def all_cyclic_shifts(text):
    mySet = set()

    for i in range(len(text)):
        partOne = text[i:len(text)]
        partTwo = text[0:i]
        word = partOne + partTwo
        mySet.add(word)
        
    myList = list(mySet)
    myList = sorted(myList)   
    
    return myList

# print(all_cyclic_shifts('01001'))

print(all_cyclic_shifts('hello'))

# make a set, 
# shift using splice maybe
# add each spliced word to set
# lenght of letters = how many splices to do
# add set to list
# sort