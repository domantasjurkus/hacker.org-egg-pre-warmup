from util import *

def reverse(encoded, key, min_number_of_spaces_expected=4):
    result = ''

    for i in range(0, len(encoded), 6):
        eggs_hex = encoded[i:i+6]
        eggs = int(eggs_hex, 16)

        for _ in range(0, 3):
            eggs = (eggs<<(24-7))|(eggs>>7)
            eggs = eggs & ((1<<24)-1)
            eggs = eggs ^ (key[eggs&0x3]<<8)
            eggs = eggs & ((1<<24)-1)

        if eggs_contain_non_printable(eggs):
            return   

        result += eggs_to_text(eggs)
    
    # hard assumption
    if 'answer' not in result:
        return

    # optimisation: if less than n spaces - skip
    # if result.count(' ') < min_number_of_spaces_expected:
    #     return

    print(key, result)
