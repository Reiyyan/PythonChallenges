def safe_squares_rooks(n, rooks):
    cSet = set()
    rSet = set()
    for x in rooks:
        cSet.add(x[0])
        rSet.add(x[1])
    
    unsafe = (len(cSet) * n) + (len(rSet) * (n-len(cSet)))
    safe = n**2 - unsafe
    
    # print(unsafe)
    # print(cSet)
    # print(rSet)

    return safe



print(safe_squares_rooks(4,[(2,3), (0,1), (2,1)]))

# 4
# 8
# [(1, 1), (3, 5), (7, 0), (7, 6)]
# 20
