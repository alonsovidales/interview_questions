def perms(string, used=set()):
    if len(string) == 1:
        return [string]

    result = []
    strList = list(string)
    for i in xrange(len(string)):
        for m in xrange(len(string)):
            aux = strList[:]
            if i != m:
                tmp = aux[i]
                aux[i] = aux[m]
                aux[m] = tmp
            result.append(aux)
            auxStr = ''.join(aux)
            if auxStr not in used:
                used.add(auxStr)
                perms(auxStr, used)
                # perms(auxStr[1:], used) All the combinations

    return used
    

for i in perms("this"):
    print i
