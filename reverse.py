from util import *

def reverse(encoded, key, min_number_of_spaces_expected=4):
    result = ''

    for i in range(0, len(encoded), 6):
        eggs_hex = encoded[i:i+6]
        eggs = int(eggs_hex, 16)

        for j in range(0, 3):
            eggs = (eggs<<(24-7))|(eggs>>7)
            eggs = eggs & ((1<<24)-1)
            eggs = eggs ^ (key[eggs&0x3]<<8)
            eggs = eggs & ((1<<24)-1)

        eggs_binary_string = decimal_to_binary_string(eggs)
        
        # optimisation: skip if any non printable chars
        if eggs_contain_non_printable(eggs_binary_string):
            return

        eggs = binary_string_to_text(eggs_binary_string)

        result += eggs

    # optimisation: if less than n spaces - skip
    if result.count(' ') < min_number_of_spaces_expected:
        return

    print(key, result)
