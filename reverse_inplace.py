def rev_in_place(string):
    for i in xrange(len(string)/2):
        aux = string[i]
        string[i] = string[len(string)-i-1]
        string[len(string)-i-1] = aux

aux = list('this is a test')
rev_in_place(aux)
print ''.join(aux)

aux = list('this is a tes')
rev_in_place(aux)
print ''.join(aux)

aux = list('')
rev_in_place(aux)
print ''.join(aux)
