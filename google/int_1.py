# Find The Longest Substring With K Unique Characters
# http://blog.gainlo.co/index.php/2016/04/12/find-the-longest-substring-with-k-unique-characters/

def search_longest_sub_str(s, k, max_substr=None):
    if max_substr is None:
        max_substr = [0]

    if len(s) < max_substr[0]:
        return max_substr[0]

    chars_in = len(set(s)) # O(n)
    if chars_in <= k and len(s) > max_substr[0]:
        max_substr[0] = len(s)
    elif chars_in < k:
        return max_substr[0]

    if len(s) > 0:
        search_longest_sub_str(s[1:], k, max_substr)
    if len(s) > 1:
        search_longest_sub_str(s[:len(s)-1], k, max_substr)

    return max_substr[0]


#print search_longest_sub_str('ababaacccccASDF123asdf', 4)

import collections

# Implementation using the freqs table:
def search_longest_sub_str_index(s, k, i=0, j=-1, max_substr=None, freqs=None):
    if max_substr is None:
        j = len(s)-1
        max_substr = [0]
        freqs = collections.Counter(s)

    if j-i+1 <= max_substr[0]:
        return max_substr[0]

    if len(freqs) <= k and j-i+1 > max_substr[0]:
        max_substr[0] = j-i+1
    elif j-i+1 <= max_substr[0]:
        return max_substr[0]

    if len(s) > i:
        if freqs[s[i]] == 1:
            del freqs[s[i]]
        else:
            freqs[s[i]] -= 1
        search_longest_sub_str_index(s, k, i+1, j, max_substr, freqs)
        freqs[s[i]] += 1


    if freqs[s[j]] == 1:
        del freqs[s[j]]
    else:
        freqs[s[j]] -= 1
    search_longest_sub_str_index(s, k, i, j-1, max_substr, freqs)
    freqs[s[j]] += 1

    return max_substr[0]

s = 'ababaacccccASDF123asdf'

for i in xrange(10):
    print "Testing:", i
    assert(search_longest_sub_str_index(s, i) == search_longest_sub_str(s, i))
