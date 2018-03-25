"""
String encode(List<String> input); 
List<String> decode(String input);
"""

ESCAPE_CHAR = '-'
SEPARATOR = ','

class EncDec(object):
    def dec(self, enc_strings):
        in_esc = False
        result = []
        curr_str = ''
        dfa_pos = 0
        for c in enc_strings:
            if c == ESCAPE_CHAR:
                if in_esc:
                    curr_str += c

                in_esc = not in_esc
            elif c == SEPARATOR:
                if in_esc:
                    curr_str += c
                    in_esc = False
                else:
                    result.append(curr_str)
                    curr_str = ''
            else:
                if in_esc:
                    curr_str += ESCAPE_CHAR+c
                    in_esc = False
                else:
                    curr_str += c

        if curr_str != '':
            result.append(curr_str)

        return result

    def enc(self, strings):
        return SEPARATOR.join(map(lambda s: s.replace(ESCAPE_CHAR, ESCAPE_CHAR*2).replace(SEPARATOR, ESCAPE_CHAR+SEPARATOR), strings))

import unittest

class TestEncDec(unittest.TestCase):
    def test_enc_dec(self):
        strings = [
            'hello',
            'this,is a -,test',
            'hio,,ew'
        ]

        encoder = EncDec()
        result = encoder.enc(strings)
        self.assertEqual(result, "hello,this-,is a ---,test,hio-,-,ew")
        self.assertEqual(encoder.dec(result), strings)

if __name__ == '__main__':
    unittest.main()
