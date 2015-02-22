def search_for(array, to):
    aux = set()
    for num in array:
        if to-num in aux:
            return to-num, num

        aux.add(num)

    return False

array = [1,2, 3, 4, 56,6 ,7, 3, 4, 6]

print search_for(array, 2)
