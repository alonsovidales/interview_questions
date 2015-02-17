def add_binary_num(num1, num2):
    res = ''
    carry = False
    maxLen = max(len(num1), len(num2))
    num1 = list(num1.zfill(maxLen))
    num2 = list(num2.zfill(maxLen))
    print num1
    print num2
    for i in xrange(maxLen-1, -1, -1):
        print num1[i], num2[i]
        if carry:
            if  num1[i] == '0' or num2[i] == '0':
                if num1[i] == '0':
                    num1[i] = '1'
                else:
                    num2[i] = '1'
            else:
                    num1[i] = '0'
            carry = True

        if num1[i] != num2[i]:
            res = '1' + res
            carry = False
        else:
            res = '0' + res
            carry = num1[i] == '1'

    if carry:
        res = '1' + res

    return res

print add_binary_num('110', '1111')
