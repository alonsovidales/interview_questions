def find_three_nums_sum_n(numbers, target=0):
    available_combinations = {}
    for n in numbers:
        if target - n in available_combinations:
            print ', '.join(map(str, available_combinations[target-n] + [n]))
            return
        for ni in numbers:
            available_combinations[n + ni] = [n, ni]
        
        
    return False
    
print find_three_nums_sum_n([4, -2, 2, -2, 20])
