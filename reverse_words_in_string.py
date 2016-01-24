# Reverse words in string

def reverse_words(in_str):
	return ' '.join(in_str.split()[::-1])

print reverse_words("hello this is a test")
