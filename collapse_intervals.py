def collapse_intervals(items):
    current = None
    end = None
    result = ''
    for i in items:
        if current == None:
            start = i
            current = i
    
        elif i == current + 1:
            current = i

        else:
            end = current
            if start == end:
                result += str(start) +','
            else:
                result += str(start) +'-' + str(end) +','
            start = i
            current = i

    end = current
    if start == end:
        result += str(start)
    else:
        result += str(start) +'-' + str(end)
    
    return result


print(collapse_intervals([1, 2, 4, 6, 7, 8, 9, 10, 12, 13]))