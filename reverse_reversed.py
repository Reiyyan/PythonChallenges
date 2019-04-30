def reverse_reversed(items):
    for i in items:
        if isinstance(i, list):
            reverse_reversed(i)
            # print("List")
    
    items.reverse()
    return items

# print(reverse_reversed([1, [2, 3, 4, 'yeah'], 5]))

# print(reverse_reversed([[[[[[1, 2]]]]]]))
# print(reverse_reversed([42, [99, [17, [33, ['boo!']]]]]))