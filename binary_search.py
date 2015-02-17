def bin_search(arr, val, pos=None):
    if pos is None:
        pos = len(arr) / 2

    if arr[pos] == val:
        return pos

    if val > arr[pos]:
        step = ((len(arr) - pos) / 2)
    else:
        step = -1 * (pos / 2)

    # Not found, don't put this line until the review
    if step <= 1 and arr[pos + step] != val:
        return None

    return bin_search(arr, val, pos + step)
    

arr = [1, 3, 4, 5, 9, 10, 12, 17, 19]
print bin_search(arr, 9)
print bin_search(arr, 17)
print bin_search(arr, 15)
print bin_search(arr, 2)
print bin_search(arr, 4)
print bin_search(arr, 6)
