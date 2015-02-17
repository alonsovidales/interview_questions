# Counting sort or key-indexed

colours = ('r', 'g', 'b')

def sort_colored_array(array):
    colours = {}
    for c in array:
        colours[c] = colours.get(c, 0) + 1

    init_pos = {}
    last_init_pos = 0
    for colour in colours:
        init_pos[colour] = last_init_pos
        last_init_pos += colours[colour]

    result = [''] * len(array)
    user_colour_pos = {}
    for i in xrange(len(array)):
        char = array[i]
        result[init_pos[char]] = char
        init_pos[char] += 1

    return result
        

print sort_colored_array(['r', 'b', 'r', 'g', 'r', 'g', 'r', 'b', 'b', 'r'])
print sort_colored_array([])
print sort_colored_array(['r'])
