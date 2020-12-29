import os
import time

def string_to_decimal(text):
    ssum = 0
    multiplier = 1
    for i in range(len(text)-1, 0-1, -1):
        ssum += ord(text[i]) * multiplier

        multiplier *= 256
    
    return ssum

def eggs_to_ints(eggs):
    egg_right = eggs % 256
    egg_middle = (eggs % (256**2) - egg_right) // 256
    egg_left = (eggs - egg_middle - egg_right) // (256**2)

    return [egg_left, egg_middle, egg_right]

def eggs_to_text(eggs):
    egg_ints = eggs_to_ints(eggs)

    a = ''.join(list(map(chr, egg_ints)))

    return a

def eggs_contain_non_printable(eggs):
    egg_ints = eggs_to_ints(eggs)

    for egg_int in egg_ints:
        if egg_int < 32 or egg_int > 126:
            return True
    
    return False

# def egg_is_alphabetical(egg_integer):
#     if integer < 65 or integer > 122:
#         return False

#     if integer < 91:
#         return True

#     if integer < 97:
#         return False
    
#     return True

# def debug_egg(egg_text):
#     while len(egg_text) % 8 != 0:
#         egg_text = '0' + egg_text
    
#     for i in range(0, len(egg_text), 8):
#         print(egg_text[i:i+8] + " ", end='')

#     print()