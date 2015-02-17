
def move_zeroes_end(num_list):
    if len(num_list) == 0:
        return num_list

    end_pos = len(num_list)-1
    while end_pos > 0 and num_list[end_pos] == 0:
        end_pos -= 1

    i = 0
    while i < len(num_list) and i <= end_pos:
        if num_list[i] == 0:
            num_list[i] = num_list[end_pos]
            num_list[end_pos] = 0
            while end_pos > 0 and num_list[end_pos] == 0:
                end_pos -= 1
        i += 1

    if num_list[end_pos] != 0:
        end_pos += 1
    return end_pos, num_list

print move_zeroes_end([1, 0, 9, 7, 5, 0, 2, 1])
print move_zeroes_end([1, 0, 9, 7, 5, 0, 0, 1])
print move_zeroes_end([])
print move_zeroes_end([0])
print move_zeroes_end([0, 0])
print move_zeroes_end([1, 2])
