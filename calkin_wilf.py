from fractions import Fraction
from collections import deque 

def calkin_wilf(n):
    i = 1
    first = Fraction(1,1)
    sequence = deque()
    # tempSequence = deque()
    sequence.append(first)
    # print (sequence)
    while(i<n):
        for dummy in range(len(sequence)):
            # print(x)
            myFraction = sequence.popleft()
            myNumerator = myFraction.numerator
            myDenominator = myFraction.denominator
            fractionOne = Fraction(myNumerator, (myNumerator + myDenominator))
            fractionTwo = Fraction((myNumerator+myDenominator), myDenominator)
            sequence.append(fractionOne)
            i+=1
            if(i == n):
                return sequence[-1]
            sequence.append(fractionTwo)
            i+=1
            if(i == n):          
                return sequence[-1]
            # print(sequence)            
    return [-1]

print(calkin_wilf(100000))