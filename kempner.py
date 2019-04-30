from fractions import Fraction

def kempner(n):
    result = Fraction(0,1)
    # print(result)
    for i in range (1,n+1):
        # denominator = 
        # print(i)
        if str(9) not in str(i):
            # print(i)
            result += Fraction(1,i)
    
    result = result.limit_denominator(1000)
    return result

# print(kempner(4))
print(kempner(100))
