comments_dfa = (
    ({
        '/': 1,
        'oth': 0,
        'in_comment': False,
    }, {
        '/': 2,
        '*': 3,
        'oth': 0,
        'in_comment': False,
    }, {
        '\n': 0,
        'oth': 2,
        'in_comment': True,
    }, {
        '*': 4,
        'oth': 3,
        'in_comment': True,
    }, {
        '/': 0,
        'oth': 3,
        'in_comment': True,
    })
)

def remove_comments(input_string):
    result = ''
    cs = 0
    comment_status = False
    for c in input_string:
        if not comments_dfa[cs]['in_comment'] or c == '\n':
            result += c

        if comments_dfa[cs]['in_comment'] and not comment_status:
            result = result[:-2]

        comment_status = comments_dfa[cs]['in_comment']

        if c in comments_dfa[cs]:
            cs = comments_dfa[cs][c]
        else:
            cs = comments_dfa[cs]['oth']

    return result

print remove_comments("""
    This is a /* test */ and / I want to check // what happends here
    123 /* Is this system */ working? or not???
    // Testing new line
""")
