# Using: Levenshtein Distance

def levenshtein_distance(s, len_s, t, len_t):
	if (len_s == 0): return len_t;
	if (len_t == 0): return len_s;

	cost = 0 if s[len_s-1] == t[len_t-1] else 1

	return min(
		levenshtein_distance(s, len_s - 1, t, len_t) + 1, # Del from s
		levenshtein_distance(s, len_s, t, len_t - 1) + 1, # Del from t
		levenshtein_distance(s, len_s - 1, t, len_t - 1) + cost) # del from both

str1 = "kitten"
str2 = "sitten"
print levenshtein_distance(str1, len(str1), str2, len(str2))

str1 = "siptin"
str2 = "sittingg"
print levenshtein_distance(str1, len(str1), str2, len(str2))
