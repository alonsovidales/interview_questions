
def search_sum_subset(integers, target, res=[]):
    if sum(integers) == target:
        res.append(integers)
    for i in xrange(len(integers)):
        search_sum_subset(integers[:i] + integers[i+1:], target, res)

    return res

integers = (1, 3, 5, 7, 8, 3)
print search_sum_subset(integers, 20)
