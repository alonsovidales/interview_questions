# does_converge(input):
# return true for convergence
# return false otherwise
# every step: sum of squares of digit of input
# e.g. input = 123
# step: 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14
# step: 14 = 1^2 + 4^2 = 1 + 16 = 17
# step: 17 = 1^2 + 7^2 = 50
# step: 50 = ...
# ...
# convergence: a -> b -> c -> d -> d -> d -> d // returns true
# a -> d -> a -> d

def does_converge(input_num):
    used_numbers = set([])
    prev_number = input_num
    
    while prev_number not in used_numbers:
        used_numbers.add(prev_number)
        aux_prev_number = prev_number
        aux = 0
        
        while aux_prev_number > 0:
            num = aux_prev_number % 10
            aux += num * num
            aux_prev_number /= 10
           
        if prev_number == aux:
            return True
        
        prev_number = aux
        
    return False

print(does_converge(123))
