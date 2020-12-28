import os
import time

def text_to_ascii_decimal(text):
    ssum = 0
    multiplier = 1
    for i in range(len(text)-1, 0-1, -1):
        ssum += ord(text[i]) * multiplier

        multiplier *= 256
    
    return ssum

def decimal_to_binary_string(decimal):
    binary = bin(decimal)[2:]

    while len(binary) % 8 != 0:
        binary = '0' + binary
    
    return binary

def binary_string_to_text(binary):
    result = ''

    for i in range(0, len(binary), 8):
        binary_char = binary[i:i+8]
        binary_int = int(binary_char, 2)
        result += chr(binary_int)
    
    return result

def eggs_contain_non_printable(bin_string):
    for i in range(0, len(bin_string), 8):
        bin_string_char = bin_string[i:i+8]
        integer = int(bin_string_char, 2)
        
        if integer < 32 or integer > 126:
            return True
    
    return False

def char_is_non_alphabet(egg_binary_string_char):
    integer = int(egg_binary_string_char, 2)
        
    if integer < 65:
        return True
    
    if integer > 122:
        return True

    if integer < 91:
        return False

    if integer < 97:
        return True
    
    return False

def debug_egg(egg_text):
    while len(egg_text) % 8 != 0:
        egg_text = '0' + egg_text
    
    for i in range(0, len(egg_text), 8):
        print(egg_text[i:i+8] + " ", end='')

    print()