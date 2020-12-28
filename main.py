import math

from util import *
from reverse import reverse

def encode(key, message):
    result = ''

    for i in range(0, len(message), 3):
        eggs = message[i:i+3]
        eggs = text_to_ascii_decimal(eggs)

        for _ in range(0, 3):
            eggs = eggs ^ (key[eggs&0x3] << 8)
            # debug_egg(bin(eggs)[2:])
            eggs = (eggs<<7)|(eggs>>(24-7))
            eggs = eggs & ((1<<24)-1)

        eggs_hex_padded = hex(eggs)[2:].zfill(6)

        result += eggs_hex_padded

    return result

key = [0, 18, 19, 20]

message = "This is a secret message"

print("Original message:")
print(message)
print()

e = encode(key, message)
print("Cypher:")
print(e)
print()

print("Decoded:")
reverse(e, key)