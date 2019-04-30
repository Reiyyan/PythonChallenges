def first_preceded_by_smaller(items, k = 1):
    for i in range(len(items)):
        count = 0
        # print(f"i is {i}")
        for x in items[0:i]:
            # print(f"range is {range(0,i)}")
            # print(f"x is {x}")
            if x < items[i]:
                # print(f"Increasing Count")
                count +=1
                if count == k:
                    return items[i]
    return None

    # For every number, see how numbers before it are smaller than it
    # if number before smaller are equal to k, return number
    # else go to next until done, then return none
    
print(first_preceded_by_smaller([4, 4, 5, 6],k=2))
print(first_preceded_by_smaller([42, 99, 16, 55, 7, 32, 17, 18, 73], k=3))
print(first_preceded_by_smaller([42, 99, 16, 55, 7, 32, 17, 18, 73], k=8))

print(first_preceded_by_smaller(['bob', 'carol', 'tina', 'alex', 'jack', 'emmy', 'tammy', 'sam', 'ted'], k=4))


