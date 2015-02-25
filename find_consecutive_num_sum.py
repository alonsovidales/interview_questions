def find_consecutive_nums_sum_x(list_num, target):
    current_value = 0
    l_p = 0
    r_p = 0
    
    while current_value != target and r_p < len(list_num):
	print l_p, r_p, current_value, target
        if target > current_value:
            current_value += list_num[r_p]
            r_p += 1
        else:
            current_value -= list_num[l_p]
            l_p += 1
            
    if current_value == target:
        return list_num[l_p:r_p]
        
    return False

num = [1, 3, 4, 5, 6, 9, 1, 2, 3, 4, 5]
print find_consecutive_nums_sum_x(num, 12)
