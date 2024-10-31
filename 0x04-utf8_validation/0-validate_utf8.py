#!/usr/bin/python3

def validUTF8(data):
    n_bytes = 0
    mask1, mask2 = 1 << 7, 1 << 6

    for num in data:
        mask = 1 << 7
        if n_bytes == 0:
            while mask & num:
                n_bytes += 1
                mask >>= 1
            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (num & mask1 and not (num & mask2)):
                return False
        n_bytes -= 1

    return n_bytes == 0