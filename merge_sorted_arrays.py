def merge_sort(arrays):
    """
    Not efficient and distroys the array param
    """
    result = []
    empty = False
    while not empty:
        minNum = float('Inf')
        empty = True
        for i in xrange(len(arrays)):
            if len(arrays[i]) > 0 and arrays[i][0] < minNum:
                empty = False
                minNum = arrays[i][0]
                minArr = i

        if not empty:
            result.append(arrays[minArr].pop(0))

    return result
            
def merge_sort_more_efficient(arrays):
    pos = [0] * len(arrays)
    print pos
    result = []
    empty = False
    while not empty:
        minNum = float('Inf')
        empty = True
        usedPos = -1
        for i in xrange(len(arrays)):
            if len(arrays[i]) > pos[i] and arrays[i][pos[i]] < minNum:
                usedPos = i
                empty = False
                minNum = arrays[i][pos[i]]

        pos[usedPos] += 1

        if not empty:
            result.append(minNum)

    return result
            

arrays = [
    [1, 3, 5, 7, 8, 9, 10],
    [4, 6, 7, 8, 10, 11, 16, 18],
    [1, 2, 4, 5, 7, 8, 9]]
print merge_sort(arrays)

arrays = [
    [1, 3, 5, 7, 8, 9, 10],
    [4, 6, 7, 8, 10, 11, 16, 18],
    [1, 2, 4, 5, 7, 8, 9]]
print merge_sort_more_efficient(arrays)
