
def intersec_sorted(arr1, arr2):
    p1 = 0
    p2 = 0
    result = []
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] == arr2[p2]:
            result.append(arr1[p1])
            p1 += 1
            p2 += 1
        elif arr1[p1] < arr2[p2]:
            p1 += 1
        else:
            p2 += 1

    return result

print intersec_sorted(
    [1, 2, 4, 6],
    [1, 2, 3, 4, 7, 9])

print intersec_sorted(
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6])

print intersec_sorted(
    [],
    [])

print intersec_sorted(
    [],
    [1, 2, 3, 4, 5, 6])

print intersec_sorted(
    [1, 2, 4, 6],
    [1, 3, 4, 7, 9])
