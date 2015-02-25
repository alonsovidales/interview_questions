max_value = 26

def get_possible_decode_combinations(encoded_str, combinations=None, total_combinations=None):
    if combinations is None:
	combinations = []
    if total_combinations is None:
	total_combinations = [0]
    if len(encoded_str) == 0:
	total_combinations[0] += 1
	return -1

    possible_combinations = []
    if encoded_str[0] != 0:
        aux = combinations[:]
	aux.append(encoded_str[0])
        get_possible_decode_combinations(encoded_str[1:], aux, total_combinations)

    if 10 <= int(encoded_str[:2]) <= 26:
        aux = combinations[:]
	aux.append(encoded_str[:2])
        get_possible_decode_combinations(encoded_str[2:], aux, total_combinations)

    return total_combinations[0]

print get_possible_decode_combinations("23")
print get_possible_decode_combinations("456")
print get_possible_decode_combinations("123")
