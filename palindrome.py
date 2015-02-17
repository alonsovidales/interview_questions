def is_pal(str_to_check):
    for i in xrange(len(str_to_check) / 2):
        if str_to_check[i] != str_to_check[-(i+1)]:
            return False

    return True

print is_pal("hello")
print is_pal("romaamor")
print is_pal("romamor")

# Could be: Manacher's algorithm, but not... this is almost the same
def get_all_palindromes_string(string):
	result = set()
	for i in xrange(len(string)-1):
		pp = 1
		while i-pp >= 0 and i+pp < len(string) and string[i-pp] == string[i+pp]:
			pp += 1

		if pp > 1:
			aux = string[i-pp+1:i+pp].strip()
			if len(aux) > 1:
				result.add(aux)

		pp = 0
		while i-pp >= 0 and i+pp+1 <= len(string) and string[i-pp] == string[i+pp+1]:
			pp += 1

		if pp > 0:
			aux = string[i-pp+1:i+pp+1].strip()
			if len(aux) > 1:
				result.add(aux)

	return result

print get_all_palindromes_string("thissi is a testtse casa perro or me  sa")
print get_all_palindromes_string("t")
print get_all_palindromes_string("")
print get_all_palindromes_string("tt")
print get_all_palindromes_string("atat")
print get_all_palindromes_string("tata")
print get_all_palindromes_string("tatr")
print get_all_palindromes_string("rtat")
