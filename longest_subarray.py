def find_longest_subarray(arr_ones, longest=None):
    if longest is None:
        longest = [[]]

    if len(arr_ones) <= 1 or arr_ones[0] <= 1:
        return

    print arr_ones
    for h in xrange(1, len(arr_ones)):
        for w in xrange(1, len(arr_ones[0])):
            aux = []
            all_ones = True
            for h_i in xrange(h+1):
                if all_ones:
                    for elem in arr_ones[h_i][:w]:
                        if elem == 0:
                            all_ones = False
                            break
                            
                aux.append(arr_ones[h_i][:w])

            if all_ones and len(longest[0]) * len(longest) < len(aux[0]) * len(aux):
                longest = aux
            find_longest_subarray(aux)

    return longest

arr_ones = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 1, 1],
    [1, 0, 1],
    [1, 0, 0]
]

print find_longest_subarray(arr_ones)

arr_ones = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1],
    [1, 1, 1],
    [1, 0, 0]
]

print find_longest_subarray(arr_ones)
