def pyramid_blocks(n, m, h):
    result = 0
    for _ in range(h):
        result += n*m
        n+=1
        m+=1
    return result

print(pyramid_blocks(10**6,10**6,10**6))